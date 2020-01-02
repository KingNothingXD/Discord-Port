const Discord = require('discord.js');
var WebSocketServer = require('websocket').server;
var http = require('http');
const bot = new Discord.Client();
const fs = require("fs");
const mongoose = require("mongoose");

// New engine
mongoose.set('useUnifiedTopology', true);

// commands collection init
bot.commands = new Discord.Collection();

bot.on('ready', () => {
  console.log("Port is online - built by Vortx")
  console.log("token: "+TOKEN)

  // search for commands & init command handler
  fs.readdir("./commands", (err, files) => {

    if(err) console.log(err); // log all errors

    let jsfile = files.filter(f => f.split(".").pop() === "js") // get rid of ".js"
    if(jsfile.length <= 0){ // if there is no content on the file
      console.log("commands not found");
      return;
    }

    jsfile.forEach((f, i) =>{ // f = file, i = number of files
      let props = require(`./commands/${f}`);
      console.log(`${f} loaded`); // log which commands have been initialized
      bot.commands.set(props.help.name, props); // set the help message to what is on the command file
    });
  });
});

var server = http.createServer(function(request, response) {
});
server.listen(1337, function() { });

// create the server
wsServer = new WebSocketServer({
  httpServer: server
});

// WebSocket server
wsServer.on('request', function(request) {
  var connection = request.accept(null, request.origin);
  // All requests and messages will be handled here
  var userName = "";

  connection.on('message', function(message) {
    if (message.type === 'utf8') {
      var content = JSON.parse(message.data);
      if (content['type']=='login' && userName=="") {
        userName=content['data']['username']

        //verification can go here later

        bot.on('message',function(message) {
          guilds = user.find({'username': userName}).guilds
          if (guilds.includes(message.guild)) {
            connection.send(JSON.stringify({'type': 'newMessage','reply': false,'data': {'content': message.content,'author': message.author.username}, 'metadata': {'guild': message.guild.id, 'channel': message.channel.id}}));
            console.log("BEEP!")
          }
        });

      }
      if (userName=="") {
        return;
      }
      if (content['type']=='requestChannel') {
        bot.channels.get(content['data']['channelId']).fetchMessages().then(function(messages) {
          connection.send(JSON.stringify({'type': 'channelHistory','data': {'content': messages}}));
        })
      }
      else if (content['type']=='requestGuilds') {
        connection.send(JSON.stringify({'type': 'guildList','data': {'content': users.find({'username': userName}).guilds}}));
      }
      else if (content['type']=='requestChannels') {
        connection.send(JSON.stringify({'type': 'guildList','data': {'content': bot.guilds.get(content['data']['guildId']).channels.forEach(function (c) {
          return {'id': c.id,'name': c.name}
        })}}));
      }
      else if (content['type']=='sendMessage') {
        bot.channels.get(content['data']['channelId']).send(content['data']['message'])
      }
    }
  });

  connection.on('close', function(connection) {
    // close user connection
  });
});

// bot config
const { prefix, TOKEN, mongousr, mongopwd } = require('./config.json');

mongoose.connect('mongodb+srv://'+mongousr+':'+mongopwd+'@cluster0-hlnlb.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true}).catch(err => console.log(err));

const user = mongoose.model('users', { username: String, password: String, salt: String, guilds: [String] });

bot.on('message', (message) => {
  // stuff to pass to commands
  let message_array = message.content.split(" ");
  let cmd = message_array[0];
  let args = message_array.slice(1);

  console.log(message.content) // for testing only

  // run handler
  if (message.author.bot) return;
  let commandfile = bot.commands.get(cmd.slice(prefix.length));
  if (commandfile) commandfile.run(bot,message,args), console.log(`${message.guild.name}: command`);

});

// run the bot
bot.login(TOKEN)

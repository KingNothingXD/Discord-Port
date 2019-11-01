var WebSocketServer = require('websocket').server;
var discord = require('discord.js');
var json = require('json')
var http = require('http');
var mongoose = require('mongoose');
var userSet = {};
mongoose.connect('mongodb://localhost:27017/port', {useNewUrlParser: true});

const user = mongoose.model('users', { username: String, password: String, salt: String, code: String });

user.find({}).then(function (users) {
  users.forEach(function (ind) {
    userSet[ind.username] = new discord.Client();
    userSet[ind.username].login(ind.code);
  });
});

var server = http.createServer(function(request, response) {
  // process HTTP request. Since we're writing just WebSockets
  // server we don't have to implement anything.
});
server.listen(1337, function() { });

// create the server
wsServer = new WebSocketServer({
  httpServer: server
});

// WebSocket server
wsServer.on('request', function(request) {
  var connection = request.accept(null, request.origin);
  // This is the most important callback for us, we'll handle
  // all messages from users here.
  var userName = "1universe";
  var thisClient = userSet[userName];
  thisClient[u].on('message',function(message) {
    connection.send(JSON.stringify({'type': 'newMessage','reply': false,'data': {'content': message.content,'author': message.author.username}, 'metadata': {'guild': message.guild.id, 'channel': message.channel.id}}));
    console.log("BEEP!")
  });
  connection.on('message', function(message) {
    if (message.type === 'utf8') {
      var content = JSON.parse(message.data);
      if (content['type']=='requestChannel') {
        thisClient.channels.get(content['data']['channelId']).fetchMessages().then(function(messages) {
          connection.send(JSON.stringify({'type': 'channelHistory','data': {'content': messages}}));
        })
      }
      else if (content['type']=='requestGuilds') {
        connection.send(JSON.stringify({'type': 'guildList','data': {'content': thisClient.guilds.forEach(function (g) {
          return {'id': g.id,'name': g.name}
        })}}));
      }
      else if (content['type']=='requestChannels') {
        connection.send(JSON.stringify({'type': 'guildList','data': {'content': thisClient.guilds.get(content['data']['guildId']).channels.forEach(function (c) {
          return {'id': c.id,'name': c.name}
        })}}));
      }
      else if (content['type']=='sendMessage') {
        thisClient.channels.get(content['data']['channelId']).send(content['data']['message'])
      }
    }
  });

  connection.on('close', function(connection) {
    // close user connection
  });
});
const Discord = require('discord.js');
const bot = new Discord.Client();
const fs = require("fs");
bot.commands = new Discord.Collection()

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

// bot config
const { prefix, TOKEN } = require('./config.json');

bot.on('message', (message) => {
  console.log(message.content) // however you want to handle message stuff here

  // stuff to pass to commands
  let message_array = message.content.split(" ");
  let cmd = message_array[0];
  let args = message_array.slice(1);

  // run handler
  if (message.author != bot){
    let commandfile = bot.commands.get(cmd.slice(prefix.length));
    if (commandfile) commandfile.run(bot,message,args)
  }
});

// run the bot
bot.login(TOKEN)

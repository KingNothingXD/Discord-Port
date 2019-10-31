const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Port is Online - Built by the Inkie Devs`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.login('token');

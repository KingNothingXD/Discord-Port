const Discord = require('discord.js');

module.exports.run = async (bot, message, args) => {
  message.channel.send("Hey ${message.author.nick}! This has yet to be added.")
  console.log("successful")
}

module.exports.help = {
  name: "get_info"
}

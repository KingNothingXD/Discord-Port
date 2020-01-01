const Discord = require('discord.js');

module.exports.run = async (bot, message, args) => {
  // search through all of the mongo db stuff for the guild
  message.channel.send(`Hey ${message.author.nick}! This has yet to be added.`);
  console.log("get_info embed not sent")
};

module.exports.help = {
  name: "get_info",
  category: "info",
  aliases: ["info", "get_info", "server_info"],
  description: "Port-related info for your server!",
  access: "all"
}

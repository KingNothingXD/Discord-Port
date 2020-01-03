const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {

  if (args[0] == "help") return message.channel.send(`try ${prefix}help instead!`); // if p!help help gets sent

  if(args[0]) {
    let command = args[0];
    if(bot.commands.has(command)) {
      command = bot.commands.get(command);
      const helpEmbed = new Discord.RichEmbed()
        .setColor('DARK_VIVID_PINK')
        .setAuthor(`Port Commands`, bot.avatarURL)
        .addField(`Command Name:`, command.name)
        .addField(`Description:`, command.description)
        .addField(`Access Level:`, command.access);
      message.channel.send(embed=helpEmbed)
    };
  };
  if(!args[0]) {
    const helpEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`Port Settings`, bot.avatarURL)
      bot.commands.forEach(command => {
        helpEmbed.addField(`${config.prefix}${command.help.name}`, `${command.help.description}`, true)
      });
    message.channel.send(embed=helpEmbed)
  };

  console.log(`help info sent to ${message.guild.name}`)
}


module.exports.help = {
  name: "help",
  category: "info",
  description: "I'm here to help",
  access: "Everyone"
}

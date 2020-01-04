const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {

  if (args[0] == "help") return message.channel.send(`try ${prefix}help instead!`); // if p!help help gets sent

  if(args[0]) { // check if a command arg is passed
    let command = args[0];
    if(bot.commands.has(command)) { // check if the bot has the command
      command = bot.commands.get(command); // get the command
      const helpEmbed = new Discord.RichEmbed()
        .setColor('DARK_VIVID_PINK')
        .setAuthor(`Port Commands`, bot.avatarURL)
        .addField(`Command Name:`, command.help.name)
        .addField(`Access Level:`, command.help.access)
        .addField(`Description:`, command.help.description)
        Object.entries(command.help.args).forEach(([key, value]) => {
          helpEmbed.addField(`${key}:`, value) // for each arg, add a field
        });
      message.channel.send(embed=helpEmbed)
    };
  };
  if(!args[0]) { // no command given
    const helpEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`Port Settings`, bot.avatarURL)
      bot.commands.forEach(command => {
        helpEmbed.addField(`${config.prefix}${command.help.name}`, `${command.help.description}`) // add a field for each command that the bot has
      });
    message.channel.send(embed=helpEmbed)
  };

  console.log(`help info sent to ${message.guild.name}`)
}


module.exports.help = {
  name: "help",
  args: {"command name":"get all relevant data for a specific command"},
  category: "info",
  description: "Need help with anything?",
  access: "Everyone"
}

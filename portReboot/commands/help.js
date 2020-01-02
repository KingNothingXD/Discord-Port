const Discord = require('discord.js');

module.exports.run = async (bot, message, args) => {

  if (args[0] == "help") return message.channel.send(`try ${prefix}help instead!`); // if p!help help gets sent

  if(args[0]) {
    let command = args[0];
    if(bot.commands.has(command)) {
      command = bot.commands.get(command);
      const helpEmbed = new Discord.RichEmbed()
        .setColor('DARK_VIVID_PINK')
        .setAuthor(`Port Settings`, message.guild.iconURL)
        .addField("Name", command.help.name)
        .addField("Description", command.help.description)
        .addField("Access Level", command.help.access);
      message.channel.send(embed=helpEmbed)
    };
  };
  if(!args[0]) {
    const helpEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`Port Settings`, message.guild.iconURL);
      // for loop over all bot.commands here
      // add a field for each one with call
    message.channel.send(embed=helpEmbed)
  };

  console.log(`help info sent to ${message.guild.name}`)
}


module.exports.help = {
  name: "help",
  category: "info",
  aliases: ["help", "h", "commands"],
  description: "I'm here to help",
  access: "all"
}

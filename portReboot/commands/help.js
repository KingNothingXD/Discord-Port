const Discord = require('discord.js');


module.exports.run = async (bot, message, args) => {
  if (args[0] == "help") return message.channel.send(`try ${prefix}help instead!`) // if p!help help gets sent

  if (args[0]) {
    let command = args[0];
    if(bot.commands.has(command)) {
      command = bot.commands.get(command);
      var helpEmbed = new Discord.RichEmbed()
      .setColor(colours.magenta)
      .setAuthor(`Port`, message.guild.iconURL)
      .setDescription(`prefix: ${prefix}`)
      .addField("Name", command.help.name)
      .addField("Description", command.help.description)
    }
  }

  message.channel.send(embed=helpEmbed)
  console.log(`help info sent to ${message.guild.name}`)
}


module.exports.help = {
  name: "help",
  category: "info",
  aliases: ["help", "h", "commands"],
  description: "I'm here to help",
  access: "all"
}

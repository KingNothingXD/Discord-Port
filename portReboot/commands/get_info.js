const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {
  // search through all of the mongo db stuff for the guild

  if(args[0]) {
    let inputGuild = args.join(" ");
    bot.guilds.forEach(guild => {
      if(guild.name == inputGuild) {
        const infoEmbed = new Discord.RichEmbed()
          .setColor('DARK_VIVID_PINK')
          .setAuthor(`${guild.name} Port Stats - Prefix: ${config.prefix}`, bot.avatarURL)
          .setThumbnail(guild.iconURL)
          .addField("Port Users", "test")
          .addField("Verification Lvl", "test")
          .addField("Port Admins", "test");
        message.channel.send(embed=infoEmbed)
      }
    });
  };

  if(!args[0]) {
    const infoEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`Port Stats - Prefix: ${config.prefix}`, bot.avatarURL)
      .setThumbnail(message.guild.iconURL)
      // Fill in with info from mongodb
      .addField("Port Users: ", "test")
      .addField("Verification Lvl", "test")
      .addField("Port Admins", "test");
    message.channel.send(embed=infoEmbed)
  };
};
module.exports.help = {
  name: "get_info",
  category: "info",
  description: "Port-related info for your server!",
  access: "all"
}

const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {
  // search through all of the mongo db stuff for the guild

  if(args[0]) {
    let inputGuild = args.join(" "); // Get the guild name
    guildFound = false; // set logic operators
    bot.guilds.forEach(guild => { // for each guild that bot has access to
      if(guild.name == inputGuild) { // does said guild's name match the input guild
        const infoEmbed = new Discord.RichEmbed() // embed
          .setColor('DARK_VIVID_PINK')
          .setAuthor(`${guild.name} Port Stats - Prefix: ${config.prefix}`, bot.avatarURL)
          .setThumbnail(guild.iconURL)
          .addField("Port Users", "test")
          .addField("Verification Lvl", "test")
          .addField("Port Admins", "test");
          guildFound = true; // logic operator
        message.channel.send(embed=infoEmbed);
      }
    });
    if (!guildFound) { // could not find guild
      message.channel.send(`Sorry, could not find the server: "${inputGuild}"`);
    }
  }

  if(!args[0]) { // assume in regards to message.guild
    const infoEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`Port Stats - Prefix: ${config.prefix}`, bot.avatarURL)
      .setThumbnail(message.guild.iconURL)
      // Fill in with info from mongodb
      .addField("Port Users: ", "test")
      .addField("Verification Lvl", "test")
      .addField("Port Admins", "test");
    message.channel.send(embed=infoEmbed)
  }
}
module.exports.help = {
  name: "get_info",
  args: {"server name": "get all port-related info about a server"},
  category: "info",
  description: "Port-related info for your server!",
  access: "all"
}

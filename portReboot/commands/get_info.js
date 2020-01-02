const Discord = require('discord.js');

module.exports.run = async (bot, message, args) => {
  // search through all of the mongo db stuff for the guild

  if(args[0]) {
    let guild = args[0];
    if(bot.guilds.has(guild)) {
      guild = bot.guilds.get(guild);
      const infoEmbed = new Discord.RichEmbed()
        .setColor('DARK_VIVID_PINK')
        .setAuthor(`${guild.name} Settings`, guild.iconURL)
        .addField("f1", "test")
        .addField("f2", "test")
        .addField("f3", "test");
      message.channel.send(embed=infoEmbed)
    };
  };
  if(!args[0]) {
    const infoEmbed = new Discord.RichEmbed()
      .setColor('DARK_VIVID_PINK')
      .setAuthor(`${message.guild.name} Settings`, message.guild.iconURL);
      // for loop over all bot.commands here
      // add a field for each one with call
    message.channel.send(embed=infoEmbed)
  };
};

module.exports.help = {
  name: "get_info",
  category: "info",
  aliases: ["info", "get_info", "server_info"],
  description: "Port-related info for your server!",
  access: "all"
}

const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {
  if (args[0]) {
    portName = args.join(" ");
    // search for port name in mongodb
    console.log(`${message.author} requested to be connected to ${portName}`);
    // send verification request to message to port account
    message.channel.send(`${message.author}, you need to accept the verification request on Port!`);
    // [ on the backend ] check every ___ secounds for accepted verifications,
    //and edit the mongodb accordngly
  } else {
    message.channel.send(`@${message.author}, please include your Port Name`);
  }

}
module.exports.help = {
  name: "connect_account",
  args: {"'Port Name'": "send a verification request to your Port account"},
  category: "info",
  description: "Connect your pre-existing Port account!",
  access: "all"
}

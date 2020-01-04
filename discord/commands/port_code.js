const Discord = require('discord.js');

const config = require('../config.json');

module.exports.run = async (bot, message, args) => {
  if (args[0]) {
    if (args == "change") {
      console.log(`port code change request`); // for testing
    } else if (args == "display") {
      console.log(`port code display request`); // for testing
    } else if (args == "-r") {
      console.log(`random code request`); // for testing
    }
  } else {
    console.log(`code dm request`); // for testing
  }
  // Search through mongodb for relevant data
  // Check if the user account is a registered port admin on said server
  // Execute arg - stipulated actions

}
module.exports.help = {
  name: "port_code",
  args: {"change": "change port code", "change -r":"change port code to a random key", "display": "DM current port code"},
  category: "info",
  description: "For all of your port_code related needs!",
  access: "all"
}

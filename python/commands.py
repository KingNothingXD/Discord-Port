def cmdName():
	cmdName = input("Display name: ")

def cmdGuild():
	cmdGuild = input("Name of server: ")
	for guild in client.guilds:
		if cmdGuild == guild.name:
			print("Now Ported to ["+cmdGuild+"]")

def cmdMessage():
	cmdMessage = input("Message: ")
	botMessage = ("[" + cmdName + "]: " + cmdMessage)
	await channel.send(botMessage)

def cmdChannel():
	cmdChannel = input("Channel: ")
	for channel in guild.channels:
		print(channel)
		for channel in guild.channels:
			if channel == channel.name:
				print("Now chatting in ["+cmdChannel+"]")
				# get channel message hsitory here


def cmdCommands():
	cmdCommand = input("Command: ")


cmdAmount = 4 # This the the amount of all of the cmdCommands, excluding cmdCommands itself.

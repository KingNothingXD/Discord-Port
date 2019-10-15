def cmdName():
	cmdName = input("Display name: ")

def cmdMessage():
	cmdMessage = input("Message: ")
	botMessage = ("[" + cmdName + "]:" + cmdMessage)
	await channel.send(botMessage)

def cmdChannel():
	cmdChannel = input("Channel: ")

def cmdGuild():
	cmdGuild = input("Name of server: ")

def cmdCommands():
	cmdCommand = input("Command: ")


cmdAmount = 4 # This the the amount of all of the cmdCommands, excluding cmdCommands itself.

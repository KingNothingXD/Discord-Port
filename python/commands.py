import json
import pathlib
from pathlib import Path
import os
import discord 
def cmdSetName():
	cmdName = input("Display name: ")
	return cmdName

async def cmdSetGuild():
	cmdGuild = input("Name of server: ")
	for guild in client.guilds:
		if cmdGuild == guild.name:
			print("Now Ported to ["+cmdGuild+"]")

async def cmdSetMessage():
	cmdMessage = input("Message: ")
	botMessage = ("[" + cmdName + "]: " + cmdMessage)


async def cmdSetChannel():
	cmdChannel = input("Channel: ")
	for channel in guild.channels:
		print(channel)
		for channel in guild.channels:
			if cmdChannel == channel.name:
				print("Now chatting in ["+cmdChannel+"]")
				# get channel message hsitory here


def cmdCommands():
	cmdCommand = input("Command: ")


cmdAmount = 4 # This the the amount of all of the cmdCommands, excluding cmdCommands itself.

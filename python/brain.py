import json
import discord
from discord import *
from discord.ext import *
import logging
import requests
from commands import get_name, get_guild, get_logs_from, get_channel_names, get_guild_names, leave_channel, command_list
import pathlib
from pathlib import Path
# Extracting the bot Token
jfile_path = Path("portJson.JSON").resolve()
with open(jfile_path, encoding='utf-8-sig') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

client = discord.Client()

async def command_command(guild, channel):
	for command in command_list:
		print(command)
	command_request = input("PCMD: ")  # ask the user for input
	tries = 0
	if command_request in command_list:  # if it exists...
		CMD_command = command_request 
	elif tries == 3:
		tries = 0
		for command in command_list:
			print(command)
		command_request = input("PCMD: ")
	else:
		print('Invalid command name, try again...')
		tries + 1
	return CMD_command
				
@client.event
async def on_ready():
	print("Port is online!")
	await get_name()
	await get_guild_names(client)
	#await get_guild(nameChoice)
	#await get_channel_names(guild)
	#for channel in guild.channels:
		#channelChoice = input("Channel Name: ")
		#for channel in guild.channels:
			#if channelChoice == channel.name:
				#print("Now in { "+channelChoice+" }")
				#await get_logs_from(channel)
				#while True:
					#messageContent = input("[ "+serverChoice+" ]"+" -"+channelChoice+"- "+" Msg: ")
					#if messageContent == "Quit":
						#break
								
					#else:
						#botMessage = ("[ "+nameChoice+" ]: "+messageContent)
						#await channel.send(botMessage)
						#await get_logs_from(channel)
	    #cmdCommand()

client.run(TOKEN)

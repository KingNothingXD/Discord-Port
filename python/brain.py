import json
import discord
from discord import *
from discord.ext import *
import logging
import requests

import pathlib
from pathlib import Path
#Bot code goes here
# Extracting the bot Token
jfile_path = Path("portJson.JSON").resolve()
with open(jfile_path, encoding='utf-8-sig') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]
jfile_pathT = Path("Test.JSON").resolve()
with open(jfile_pathT, encoding='utf-8-sig') as jsonTest:
    rawFile = json.load(jsonTest)
    serverDetails = rawFile["serverDetails"]
    takenNames = rawFile["takenNames"]
    blockedAccounts = rawFile["blockedAccounts"]

client = discord.Client()

command_list = ["{get_logs_from}", "{get_channel_name}", "{get_guild_names}", "{leave_channel}"]

async def get_name():
	nameChoice = input("Display name: ")
	if nameChoice in takenNames: # If name has been already registered
		namePword = input("Password: ")
		while nameChoice in takenNames and namePword != takenNames[nameChoice]: # If password doesn't match the one provided with the name
			print("Auth Failed")
			nameChoice = input("Display name: ")
			namePword = input("Password: ")
		print("Hi {"+nameChoice+"}!")
	else:
		save = input("Hi "+nameChoice+"! Save your name? (Y/n):")
		if save == "Y":
			print("Your Name and password are now saved!") # appened new password to 12345678.JSON here
		else:
			print("Ok then!")
	return nameChoice
async def get_guild(nameChoice):
	for guild in client.guilds:
		serverChoice = input("Server to access: ")
		serverKey = input("Server key: ") # Asks for Auth Key
		if serverChoice == guild.name: # Checks if server exists or not
			while nameChoice in blockedAccounts and serverKey == blockedAccounts[nameChoice]: # If the key provided does match with the value in the dict	
				print("This account is banned from [ "+blockedAccounts[nameChoice]+" ]")
				exit()
			while serverChoice in serverDetails and serverKey != serverDetails[serverChoice]: # If the key provided doesn't match with the value in the dict	
				print("Server key auth failed")
				serverChoice = input("Server to access: ")
				serverKey = input("Server key: ")
			print("Now ported to [ "+serverChoice+" ]")
			guild = guild.name
			return guild
async def get_logs_from(channel):
	message5 = []
	async for m in channel.history(limit=5):
		message5.append("["+ str(m.author.name)+"] "+ m.clean_content)
	message5.reverse()
	for elem in message5:
		print (elem)
	message5 = []

async def get_channel_names(guild):
	for channel in guild.channels:
		print("[ "+str(channel)+" ]")
async def get_guild_names():
	for guild in client.guilds:
		print("[ "+str(guild)+" ]")
async def leave_channel(guild):
	if messageContent == "Quit":
		print("Test confirmed")
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
	await get_guild_names()
	await get_guild(nameChoice)
	await get_channel_names(guild)
	for channel in guild.channels:
		channelChoice = input("Channel Name: ")
		for channel in guild.channels:
			if channelChoice == channel.name:
				print("Now in { "+channelChoice+" }")
				await get_logs_from(channel)
				while True:
					messageContent = input("[ "+serverChoice+" ]"+" -"+channelChoice+"- "+" Msg: ")
					if messageContent == "Quit":
						break
								
					else:
						botMessage = ("[ "+nameChoice+" ]: "+messageContent)
						await channel.send(botMessage)
						await get_logs_from(channel)
	    #cmdCommand()

client.run(TOKEN)

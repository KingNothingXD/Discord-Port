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




@client.event
async def on_ready():
	print("Port is online!")
	for guild in client.guilds:
		serverChoice = input("Server to access: ")
		if serverChoice == guild.name: # Checks if server exists or not
			serverKey = input("Server key: ") # Asks for Auth Key
			while serverChoice in serverDetails and serverKey != serverDetails[serverChoice]: # If the key provided doesn't match with the value in the dict	
				print("Server key auth failed")
				serverChoice = input("Server to access: ")
				serverKey = input("Server key: ")
			print("Now ported to [ "+serverChoice+" ]")
			nameChoice = input("Display name: ")
			if nameChoice in takenNames: # If name has been already registered
				while nameChoice in blockedAccounts and serverKey == blockedAccounts[nameChoice]: # If the key provided does match with the value in the dict	
					print("This account is banned from [ "+blockedAccounts[nameChoice]+" ]")
					exit() # Kills port on the person's PC
					# Find a better solution, that maybe has a 30 sec cooldown on their IP (for Web app)
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
			for channel in guild.channels:
				print("[ "+channel.name+" ]")
				channelChoice = input("Channel Name: ")
				for channel in guild.channels:
					if channelChoice == channel.name:
						print("Now in { "+channelChoice+" }")
						for message in str(channel.history(limit=5)):
							msg = await channel.get_message(id)
							print(msg.content)
						while True:
							messageContent = input("[ "+serverChoice+" ]"+" -"+channelChoice+"- "+" Msg: ")
							if messageContent == "Quit":
								break
							else:
								botMessage = ("[ "+nameChoice+" ]: "+messageContent)
								for message in str(channel.history(limit=5)):
									msg = await channel.get_message(id)
									print(msg.content)
		else:
			serverChoice = input("Server to access: ")
	    #cmdCommand()

client.run(TOKEN)

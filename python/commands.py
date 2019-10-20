import discord
import json
import pathlib
from pathlib import Path
from ipFinder import save_IP, get_IP, save_name_password
import socket
jfile_pathT = Path("Test.JSON").resolve()
with open(jfile_pathT, encoding='utf-8-sig') as jsonTest:
    rawFile = json.load(jsonTest)
    serverDetails = rawFile["serverDetails"]
    takenNames = rawFile["takenNames"]
    blockedAccounts = rawFile["blockedAccounts"]
jfile_pathN = Path("names.JSON").resolve()
with open(jfile_pathN, encoding='utf-8-sig') as jsonIP:
    namesRaw = json.load(jsonIP)
    names = namesRaw["IP"]

command_list = ["{get_logs_from}", "{get_channel_name}", "{get_guild_names}", "{leave_channel}"]

async def get_name():
	nameChoice = input("Display name: ")
	host_ip = get_IP()
	if host_ip in namesRaw:
		namePword = input("Password: ")
		while nameChoice in takenNames and namePword != takenNames[nameChoice]: # If password doesn't match the name set one
			print("Auth Failed")
			nameChoice = input("Display name: ")
			namePword = input("Password: ")
		print("Hi {"+nameChoice+"}!")
	else:
		save = input("Hi "+nameChoice+"! Save your name? (Y/n):")
		if save == "Y":
			save_name_password(nameChoice)
		else:
			confirm = ("Some servers have verificaton rules. Continue? (Y/n)")
			if confirm == "Y":
				save_name_password(nameChoice)
				#also check if the server allows uunverified names
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
async def get_guild_names(client):
	for guild in client.guilds:
		print("[ "+str(guild)+" ]")
async def leave_channel(guild):
	if messageContent == "Quit":
		print("Test confirmed")


import discord
from discord import *
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import os
from os import path
import json
import pathlib
from pathlib import *

basepath = path.dirname(__file__)
tokenPath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(tokenPath, 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

client = discord.Client()
bot = commands.Bot(command_prefix = "p!")

serverLogsList = os.listdir('serverLogs')
serverSettingsList = os.listdir('serverSettings')

defualtSettings = (
			Password = "123" \n
			blockedPorters = [] \n
			SV lvl = 0 \n
			)

@client.event
async def on_ready():
	print("Port is online - Built by Vortex")


@client.event
async def on_message(message):
	content = message.content					
	channel = str(message.channel)
	author = str(message.author)
	timestamp = str(message.created_at)
	messageData = ('"'+timestamp+'" = ["'+author+'", "'+channel+'", "'+content+'"] \n')
	serverTXT = (str(message.guild.id)+'.txt')
		
	if (str(message.guild.id)+'.txt') in serverLogsList:
		with open(os.path.join(os.path.abspath('serverLogs'),serverTXT), 'a') as serverData
		serverData.write(messageData)
		if (str(message.guild.id)+'.txt' not in serverSettingsList:
			with open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'w+') as settingsData:
			settingsData.write(defualtSettings)
		
	else:
		newFile = open(os.path.join(os.path.abspath('serverLogs'),serverTXT), 'w+')
		newFile.write(messageData)
		newFile.close()
		serverSettings = open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'w+')
		serverSettings.write(defualtSettings)
		serverSettings.close()
	print (f"Message Sent in {message.guild.name} by {message.author.name}")
	await bot.process_commands(message)

async def serverSettingsEmbed(message):
	serverTXT = (str(message.guild.id)+'.txt')
	with open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'r') as serverSettings:
		data = severSettings.readlines()
	pword = []
	blocked = []
	sv = []
	for line in serverSettings:
		if ("password") in line:
			pword.append(line)
		    	del pword["password", "="]
		    	print (pword)# for testing purposes, remove when it works
		elif ("blockedPorters") in line:
			blocked.append(line)
		    	del blocked["blockedPorters", "="]
		   	print (blocked)# for testing purposes, remove when it works
		elif ("SV lvl") in line:
			sv.append(line)
		    	del sv["sv lvl", "="]
		    	print (sv)# for testing purposes, remove when it works
		# get the respective list of the settings here 
		# https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file
	serverSettingsEmbed=discord.Embed(title="Settings", description="your Port settings for "+message.guild.name, color=0xda00ff)
	serverSettingsEmbed.add_field(name="Server Password [p!pwrd (new password)]", value="serverPassword", inline=False)
	serverSettingsEmbed.add_field(name="Blocked Porters [p!block (port display name)]", value="blockedUsers", inline=False)
	serverSettingsEmbed.add_field(name="SV lvl [p!SV (new verification level)]", value="serverVLevel", inline=False)
	await bot.send_message(message.channel, embed=serverSettingsEmbed)

async def serverChangeSettings(message):
	serverName = (str(message.guild.id)+'.txt')
	serverSettings = open(os.path.join(os.path.abspath('serverSettings'),serverName), 'a')
		# get the list of settings here
	await message.channel.send("Server Settings Updated")


@bot.command(name='settings')
async def serverSettings(message):
	if message.author.server_permissions.administrator:
		await serverSettingsEmbed(message)
	else:
		await message.channel.send("Sorry, you can't see this without permissions")		

@bot.command(name='change settings')
async def changeSettings(message):
	if message.author.server_permissons.administrator:
		await serverSettingsEmbed(message)
		await changeServerSettings(message)
		await serverSettingsEmbed(message)
	else:
		await message.channel.send("Sorry, you are not authorized to do that")
		    
async def settingsHelpEmbed(message):
	serverSettingsHelpEmbed=discord.Embed(title="Settings Help", description"I give you great aid in your time of need", color=0xda00ff)
	serverSettingsHelpEmbed.add_field(name="Set Server Password", value="p!pwrd (new password)", inline=False)
	serverSettingsHelpEmbed.add_field(name="Blocked a Port User", value="p!block (port display name)", inline=False)
	serverSettingsHelpEmbed.add_field(name="Set Server Verification Level", value="p!SV (0-3)", inline=False)
	serverSettingsHelpEmbed.add_field(name="Server Verifications Levels Explained", value="0 = Wild West: no restrictions \n 1 = Christian Minecraft Server: no cursewords in name \n 2 = Grandma's House: no offensive names \n 3 = Fort Knox: only names of members on the server", inline = False)
	await message.author.send(embed=serverSettingsHelpEmbed)
@bot.command(name='settings help')
async def settingsHelp(message):
	if message.author.server_permissons.administrator:
		await settingsHelpEmbed(message)
	else:
		await message.author.send("Sorry, you must have administrator to use this command") 
#@botClient.command(name='pwrd'):
	# take args for password here and check verifacation

botClient.run(TOKEN)
		

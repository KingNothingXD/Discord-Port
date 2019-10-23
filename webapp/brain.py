import discord
from discord import *
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

serverLogsList = os.listdir("serverLogs")


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
		openServerData = open(os.path.join(os.path.abspath('serverLogs'),serverTXT), 'a')
		openServerData.write(messageData)
		openServerData.close()
		if (str(message.guild.id)+'.txt' in serverSettingsList:
			openSettingsData = open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'a')
			openSettingsData.write(newSettings)
			openSettingsData.close()
		
	else:
		newFile = open(os.path.join(os.path.abspath('serverLogs'),serverTXT), 'w+')
		newFile.write(messageData)
		newFile.close()
		serverSettings = open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'w+')
		serverSettings.write(defualtSettings)
		serverSettings.close()
	print (f"Message Sent in {message.guild.name} by {message.author}")
	await bot.process_commands(message)
			

async def serverSettingsEmbed(message):
	serverTXT = (str(message.guild.id)+'.txt')
	serverSettings = open(os.path.join(os.path.abspath('serverSettings'),serverTXT), 'r')
		# get the respective list of the settings here 
		# https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file
	serverSettingsEmbed=discord.Embed(title="Settings", description="your Port settings for "+"message.guild.name", color=0xda00ff)
	serverSettingsEmbed.add_field(name="Server Password [p!pwrd (new password)]", value="serverPassword", inline=False)
	serverSettingsEmbed.add_field(name="Blocked Porters [p!block (port display name)]", value="blockedUsers", inline=False)
	serverSettingsEmbed.add_field(name="SV lvl [p!SV (new verification level)]", value="serverVLevel", inline=False)
	await botClient.send_message(message.channel, embed=serverSettingsEmbed)

@bot.command(name='server')
async def serverSettings(message):
	if message.author.server_permissions.administrator:
		await serverSettingsEmbed(message)
	else:
		await message.channel.send("Sorry, you don't have permissions....")		

#@botClient.command(name='pwrd'):
	# take args for password here and check verifacation

botClient.run(TOKEN)
		

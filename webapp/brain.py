import discord
from discord import *
import json
import os
from os import path

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(filepath, encoding='utf-8-sig', 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

client = discord.Client(command_prefix="p!")

serverFilesList = os.listdir("serverFiles")

async def on_message(message):
	await client.wait_until_ready()
	while not client.is_closed:
		content = message.content					
		channel = message.channl
		author = message.author
		messageData = ('"'+channel+'": '+'{"'+author+'": "'+content+'"}'
		for f in range(serverFileList):
			if str(message.guild.id) == os.path.basename(file):
				with open ((guild.id + '.JOSN')) as f:
					fileData = json.load(f)
				fileData.update(messageData)
				with open ((guild.id + '.JSON'), 'w') as messageFile:
					json.dump(fileData, messageFile)


@client.event
async def on_ready():
	print("Port is online - Built by Vortex")
	
@client.event
async def on_guild_join():
	with open((guild.id + '.JSON'), 'w') as guildfile:
		json.dump(guildfile)

client.loop.create_task(on_message())
client.run(TOKEN)
		

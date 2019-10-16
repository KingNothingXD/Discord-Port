import discord
from discord.utils import get
from pprint import pprint
import json
import pathlib
from pathlib import Path
from discord import User
from discord.ext import commands
from discord.ext.commands import Bot
from commands import *

descrip = "A discord port to a webpage/machine written by NotU. Check out my Github!"
client = discord.Client()

# Extracting the bot Token
jfile_path = Path("portJson.JSON").resolve()
with open(jfile_path, encoding='utf-8-sig') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]
# Extracting the taken Names
jname_path = Path("takenNames.JSON").resolve()
with open(jname_path, encoding='utf-8-sig') as jName:
	rawName = json.load(jName)

async def sendMessage():
	await channel.send(botMessage)
@client.event
async def on_ready():
	print("Port is online!")
	cmdSetName()
	if cmdName != "": # This executes if cmdName has a value.
		#cmdCommand() # Move all of the spagat below into this command (possibly using a while statement)
		while cmdName in rawName: # if cmdName is a takenName
			await cmdSetName()
		else:
			await cmdSetGuild()
			await cmdSetChannel()
			await cmdSetMessage()
			await sendSetMessage()					
											
client.run(TOKEN)

import discord
from discord import *
from discord.ext import *
import logging
import requests
from usermessages import #import the message related commands here

import pathlib
from pathlib import Path
#Extracting the bot Token
jfile_path = Path("portToken").resolve()
with open(jfile_path, encoding='utf-8-sig') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

prefix = "p!"
client = discord.Client(command_prefix=prefix)

@client.event
async def on_ready():
	print( "Port Online - [Built by Ben]")
	
@client.command
async def set_password():
	#check if message.author has admin perms
	#change guild password

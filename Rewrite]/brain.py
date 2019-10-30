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

from logic import messageData

basepath = path.dirname(__file__)
tokenPath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(tokenPath, 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

client = discord.Client()
bot = commands.Bot(command_prefix = "p!")

@client.event
async def on_ready():
	print("Port is online - Built by Vortex")


@client.event
async def on_message(message):
	displayMessage(message)
	 # This is a private var, so it will be reset everytime a message is sent		
	print (f"Message Sent in {message.guild.name} by {message.author.name}")
	await bot.process_commands(message)

client.run(TOKEN)
		

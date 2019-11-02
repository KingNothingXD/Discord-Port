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
from cmds import helpCommand
from cmds import botCommands
from logic import messageData


basepath = path.dirname(__file__)
tokenPath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(tokenPath, 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

bot = commands.Bot(command_prefix = "p!")
bot.remove_command('help') # This gets rid of the default help command

@bot.event
async def on_ready():
	print("Port is online - Built by Vortex")
	bot.add_cog(messageData(message))
	bot.add_cog(botCommands(message))
	bot.add_cog(helpCommand(message))

bot.run(TOKEN)

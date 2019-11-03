import discord
from discord import *
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.client import *
import os
from os import path

from pymongo import MongoClient
mongoClient = MongoClient('<<MongoDB URL>>’)

import json

import pathlib
from pathlib import *

from cmds import botCommands
from logic import logData


basepath = path.dirname(__file__)
tokenPath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(tokenPath, 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

bot = commands.Bot(command_prefix = "p!")
bot.remove_command('help') # This gets rid of the default help command


@bot.command(brief="Help Command [ p!help ]")
async def help(message):
	helpEmbed = discord.Embed(color=0x00ffe4)
	helpEmbed.set_author(name="Port Help")
	for command in bot.commands:
		helpEmbed.add_field(name=command.name, value=command.brief, inline=False)
	helpEmbed.set_footer(text="Port is built and maintained by Vortex")
	await message.author.send(embed=helpEmbed)
	await message.channel.send(f"Hey {message.author.nick}, I just DM'd you the help info!")

@bot.event
async def on_ready():
	print("Port is online - Built by Vortex")
	bot.add_cog(logData(message))
	bot.add_cog(botCommands(message))
	await bot.change_presence(activity=Game(name='telephone'))
	# have this be the amount of online clients on port
		
		# put the Port help embed here

bot.run(TOKEN)

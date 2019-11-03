import discord
from discord import *
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.client import *
import os
from os import path

import json

import pathlib
from pathlib import *

from cmds import botCommands
from logic import messageData


basepath = path.dirname(__file__)
tokenPath = path.abspath(path.join(basepath, "..", "..", "portToken.JSON"))

with open(tokenPath, 'r') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

bot = commands.Bot(command_prefix = "p!")
bot.remove_command('help') # This gets rid of the default help command


@bot.command(description="Help Command [ p!help ]")
async def help(message):
	helpEmbed = discord.Embed(title="Port Help", description=f"Help with Port commands on {message.guild.name}", inline=True, color=0x00ffe4)
	for command in bot.commands:
		try:
			helpEmbed.add_field(name=command.name, value=str(command.description), inline=False)
		except:
			helpEmbed.add_field(name="Sorry", value="Error", inline=False)
	helpEmbed.set_footer(text="Port is built and maintained by Vortex")
	await client.send_message(message.author, embed=helpEmbed)

@bot.event
async def on_ready():
	print("Port is online - Built by Vortex")
	bot.add_cog(messageData(message))
	bot.add_cog(botCommands(message))

		
		# put the Port help embed here

bot.run(TOKEN)

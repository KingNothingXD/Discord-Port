# Discord imports
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot

# All external file handling
import os
from os import path
import json
from pathlib import Path
from cmds import botCommands
from logic import logData

# Getting the bot token from the server file system
tokenPath = Path("portToken.JSON").resolve()

with open(tokenPath, 'r') as j:
	rawFile = json.load(j)
	TOKEN = rawFile['TOKEN']

# Remove the defualt help command, set the prefix
bot = commands.Bot(command_prefix = "p!")
bot.remove_command('help')

# Custom help command
@bot.command(brief="Help Command [ p!help ]")
async def help(message):
	helpEmbed = discord.Embed(color=0x00ffe4)
	helpEmbed.set_author(name="Port Help")
	for command in bot.commands:
		helpEmbed.add_field(name=command.name, value=command.brief, inline=False)
	helpEmbed.set_footer(text="Port is built and maintained by Vortex")
	await message.author.send(embed=helpEmbed)
	try:
		await message.channel.send(f"Hey {message.author.nick}, I just DM'd you the help info!")
	except None:
		print(f"Could not find a nick for {message.author}.")
		await message.channel.send(f"Hey {message.author.name}, I just DM'd you the help info!")
		
# When bot comes online; do
@bot.event
async def on_ready():
	print("Port is online - Built by Vortex")
	# Load cogs
	bot.add_cog(botCommands(message))
	
	# Change the bot's presence (This could be changed to something else later)
	await bot.change_presence(activity=Game(name='telephone'))
	
# Run the bot
bot.run(TOKEN)

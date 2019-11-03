import discord
from discord import *
from discord.ext import commands

bot = commands.Bot(command_prefix = "p!")

class botCommands(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.command(discription="Register your discord account on Port [ p!register ]")
	async def register(self, message):
		await message.channel.send("This feature has yet to be implemented! Hang in there!")
		# create a message for verifacation
	@commands.command(discription="Server specific information regarding port [ p!info ]")
	async def info(self, message):
		await message.channel.send("Server specific port info will go here!")
		# put the guild specific  port info here
	@commands.command(description="Change your server's Port settings [ p!changesettings ]")
	async def changesettings(self, message):
		await message.channel.send("This has yet to be set up! Stay tuned")
		# put the dm server admin stuff here


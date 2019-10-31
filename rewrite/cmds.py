import discord
from discord import *
from discord.ext import commands

class botCommands(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.Cog.listener()
	async def on_member_join(self, member):
		# dm member server specific port info
		pass # for now
	@commands.command()
	async def register(self, message):
		await message.channel.send("This feature has yet to be implemented! Hang in there!")
		# create a message for verifacation
	@commands.command()
	async def info(self, message):
		await message.channel.send("Server specific port info will go here!")
		# put the guild specific  port info here
	@commands.command()
	async def changesettings(self, message):
		await message.channel.send("This has yet to be set up! Stay tuned")
		# put the dm server admin stuff here
	@commands.command()
	async def help(self, message):
		await message.channel.send("The custom help embed goes here!")
		# put the Port help embed here

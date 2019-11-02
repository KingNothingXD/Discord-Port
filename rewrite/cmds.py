import discord
from discord import *
from discord.ext import commands

bot = commands.Bot(command_prefix = "p!")

class botCommands(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.command("register")
	async def register(self, message):
		description = "Register your discord account on Port"
		await message.channel.send("This feature has yet to be implemented! Hang in there!")
		# create a message for verifacation
	@commands.command("info")
	async def info(self, message):
		description = "Server specific information regarding port"
		await message.channel.send("Server specific port info will go here!")
		# put the guild specific  port info here
	@commands.command("changesettings")
	async def changesettings(self, message):
		description = "Change your server's Port settings"
		await message.channel.send("This has yet to be set up! Stay tuned")
		# put the dm server admin stuff here

class helpCommand(commands.Cog):
	# instance Attributes - on init
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command("help")
	async def help(self, message):
		description="Help Command"
		helpEmbed = discord.Embed(title="Port Help", description=f"Help with Port commands on {message.guild.name}", color=0x00ffe4)
		for command in bot.Commands:
			helpEmbed.add_field(name=command.name, value=description, inline=False)
		helpEmbed.set_footer(text="Port is built and maintained by Vortex")
		await message.channel.send(embed=helpEmbed)
		
		# put the Port help embed here

import discord
from discord import *
from discord.ext import commands

bot = commands.Bot(command_prefix = "p!")

class botCommands(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot, commands):
		self.bot = bot
	# instance method
	@commands.command(name="register", description = "Register your discord account on Port")
	async def register(self, message):
		await message.channel.send("This feature has yet to be implemented! Hang in there!")
		# create a message for verifacation
	@commands.command(name="info", description = "Server specific information regarding port")
	async def info(self, message):
		await message.channel.send("Server specific port info will go here!")
		# put the guild specific  port info here
	@commands.command(name="changesettings", description = "Change your server's Port settings")
	async def changesettings(self, message):
		await message.channel.send("This has yet to be set up! Stay tuned")
		# put the dm server admin stuff here
	@commands.command(name="help", description="Help Command")
	async def help(self, ctx):
		helpEmbed = discord.Embed(title="Port Help", description="Help with Port commands on {ctx.guild.name}", color=0x00ffe4)
		for command in bot.commands:
			helpEmbed.add_field(name=command(name), value=command(description), inline=False)
		helpEmbed.set_footer(text="Port is built and maintained by Vortex")
		await ctx.channel.send(embed=helpEmbed)
		
		# put the Port help embed here

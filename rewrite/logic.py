
import discord
from discord import *
from discord.ext import commands


class logData(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.Cog.listener()
	async def on_message(self, message):
		guildTag = str(message.guild.id) + ".txt" # The file extension should be whatever mongoDB uses
		
		# check a message contains any other media (Mention, Image, Link, (so far))
		# assign either True or False to each respective variable
		# have the front/backend have a system for using this data (mentioned get a notification, link has a thumbnail, etc.)
		author = message.author.name
		content = message.content
		channel = message.channel
		time = message.created_at
		if guildTag in logFolders:
			# append the guild logs with the new message and it's data in the agreed upon form
			pass # for now
		# if there is no existing guild log
		# create a new log with guildTag




import discord
from discord import *
from discord.ext import commands

from pymongo import MongoClient


class logData(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method

	@commands.Cog.listener()
	async def on_message(self, message):
		mongo = pymongo.MongoClient("mongodb+srv://sudo:<theducksaysmoo>@messages-hlnlb.mongodb.net/test?retryWrites=true&w=majority")
		messagesDB = mongo.messages
		guildTag = str(message.guild.id)
		if guildTag in messagesDB.list_collection_names():
			print(f"connected to {message.guild.name}")
		else:
			messagesDB.create_collection(guildTag)
			print(f"created {message.guild.name} logs")
		# check a message contains any other media (Mention, Image, Link, (so far))
		# assign either True or False to each respective variable
		# have the front/backend have a system for using this data (mentioned get a notification, link has a thumbnail, etc.)
		messageDict = {}
		messageDict['author'] = message.author.nick
		messageDict['content'] = message.content
		messageDict['channel'] = message.channel
		messageDict['time'] = message.created_at
		guildTag.insert_one(messageDict)
		# if there is no existing guild log
		# create a new log with guildTag



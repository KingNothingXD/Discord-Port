
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
		#pass information from requests here
		pass



import flask
import json
import discord
from discord import *
from discord.ext import commands


class messageData(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.Cog.listener()
	async def on_message(self, message):
		msgs = await message.channel.history(limit=10).flatten()
		for message in reversed(msgs):
			author = message.author.name
			content = message.content
			channel = message.channel
			guild = message.guild
			time = message.created_at
			if content:
				print (f"{author} said: {content}")
				continue
			else:
				continue


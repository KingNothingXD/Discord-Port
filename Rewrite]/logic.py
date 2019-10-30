import flask
import json
import discord

class messageData:
	
	# instance Attributes - on Init
	def __init__(self, message):
		self.message = messageObject
		self.message.author.name = author
		self.message.content = content
		self.message.channel = channel
		self.message.guild = guild
		self.message.created_at = time
	
	# instance method
	def displayMessage(self, message): #put whatever the thing for writing a message in flask is here
		for message in channel.history(limit=30):
			print(author + content + channel + guild + str(time))
		# display message in respective guild and channel, with name.
			


import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix = "p!")

vortex = ["473446958414037022", "292293847567040512"]
# Set the Vortex var to based on who has the devOps or founder role.

class botCommands(commands.Cog):
	# instance Attributes - on Init
	def __init__(self, bot):
		self.bot = bot
	# instance method
	@commands.command(brief="Used by Vortex")
	async def downtime(self, downtime, reason):
		if str(message.author.id) in vortex:
			print("Message Author Confimed")
			embed = discord.Embed(color=0x00ffe4)
			embed.set_author(name="Port Downtime")
			embed.add_field(name="Estimated Downtime", value=(str(downtime)+" Hours"), inline=False) 
			embed.add_field(name="Reason", value=str(reason), inline=False)
			for channel in client.get_all_channels():
				if "port" in channel.name.lower():
					try:
						await channel.send(embed=embed)
						print(f"Downtime Message Sent to {channel.guild.name}!")
					except Error:
						print(f"Error sending message to {channel.guild.name}!")
					
	@commands.command(brief="Register your discord account on Port [ p!register ]")
	async def register(self, message):
		await message.author.send(f"Hi {message.author.nick}! Lets hook you up to Port!")
		# guild specific nicknames should remain the same, use user ID to get the nickname for the given guild on Port
		await message.channel.send("This feature has yet to be implemented! Hang in there!")
		
	@commands.command(brief="Connect your Discord account to a pre-existing Port account [ p!verify ]")
	async def verify(self, message):
		await message.author.send(f"Hey {message.author.nick}! How about we verify that Port account!")
		await message.author.send(f"{message.author.nick}, type in the Port name and hex you would like to connect to your Discord!")
		# listen for a port account name and hex, else, display a verify help-embed
		# create a message for Discord account verifacation
		
	@commands.command(brief="Server specific information regarding port [ p!info ]")
	async def info(self, message):
		await message.channel.send("Server specific port info will go here!")
		# put the guild specific  port info here
		# check if the message author has permissions of admin or higher
			#send an admin version of the server about page
		# if the message author does not have server perms of admin or higher
			#send the normal server about page
			# ex. people who can change server settings
			# ex. how many Porters are blocked from this server
			# ex. the SV lvl of the server
			
			#have both what the admin and normal server about pages display be customizable by admin or higher in change server settings
		
		
	@commands.command(brief="Change your server's Port settings [ p!changesettings ]")
	async def changesettings(self, message):
		# check if message author has permissions of admin or higher
			# have change settings process
		# else, send a message to the channel saying you don't have permisions!
		# add a tick to a counter that is linked to the message.author's ID
		# if the message.author has ____ amount of strikes, dm that they will be added to a list of people to review Port membership if they continue
		await message.channel.send("This has yet to be set up! Stay tuned")
		# put the dm server admin stuff here


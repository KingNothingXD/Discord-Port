from servers import serverSelection, nameSelection # Server data
import json
import discord
import pathlib
from pathlib import Path
#Bot code goes here
# Extracting the bot Token
jfile_path = Path("portJson.JSON").resolve()
with open(jfile_path, encoding='utf-8-sig') as jPort:
	rawFile = json.load(jPort)
	TOKEN = rawFile["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print("Port is online!")
    serverList = client.guilds
    serverSelection()
    if serverChoice in client.guilds:
        print("Now ported to [ "+serverChoice+" ]")
        nameSelection()
        for i in range(len(guild.channels)):
	        print("[ "+guild.channels[i]+" ]")
	        logs = client.logs_from(channelChoice, limit=10)
    else:
        serverSelection()
	    #cmdCommand()

client.run(TOKEN)

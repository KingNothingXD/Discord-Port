import json
import pathlib
from pathlib import Path
import discord

jfile_path = Path("12345678.JSON").resolve()
with open(jfile_path, encoding='utf-8-sig') as jsonFile:
    rawFile = json.load(jsonFile)
    serverDetails = rawFile["serverDetails"]
    takenNames = rawFile["takenNames"]
    blockedAccounts = rawFile["blockedAccounts"]

def serverSelection():
    for i in range(len(serverList)):
        print("[ "+serverList[i]+" ]") # Prints all of the Items of server list
    serverChoice = input("Server to access: ")
    while serverChoice not in serverList: # Checks if server exists or not
        print("server doesn't exist")
        serverChoice = input("Server to access: ")
    serverKey = input("Server key: ") # Asks for Auth Key
    while serverChoice in serverDetails and serverKey != serverDetails[serverChoice]: # If the key provided doesn't match with the value in the dict
        print("Server key auth failed")
        serverChoice = input("Server to access: ")
        serverKey = input("Server key: ")

    
def nameSelection():
    nameChoice = input("Display name: ")
    if nameChoice in takenNames: # If name has been already registered
        if nameChoice in blockedAccounts: # If name has been blocked on a server
            print("This account is banned from [ "+blockedAccounts[nameChoice]+" ]")
            exit() # Kills port on the person's PC
                    # Find a better solution, that maybe has a 30 sec cooldown on their IP (for Web app)
        namePword = input("Password: ")
        while nameChoice in takenNames and namePword != takenNames[nameChoice]: # If password doesn't match the one provided with the name
            print("Auth Failed")
            nameChoice = input("Display name: ")
            namePword = input("Password: ")
        print("Hi {"+nameChoice+"}!")
    else:
        save = input("Hi "+nameChoice+"! Save your name? (Y/n):")
        if save == "Y":
            print("Your Name and password are now saved!") # appened new password to 12345678.JSON here
        else:
            print("Ok then!")

def sendMessage():
    messageContent = input("Msg: ")
    botMessage = ("[ "+nameChoice+" ]: "+messageContent)
    await channel.send(botMessage)

def channelChoice():
    channelContent = input("Channel: ")
    if channelContent in guild.channels:
        print("Huzzah!")
    else:
        print("Non-existant")

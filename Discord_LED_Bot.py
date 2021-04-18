import discord
import re
import requests

serverIP=""
discordToken=""

colourDict={
    "blue": (0,0,255),
    "blau": (0,0,255),
    "red": (255,0,0),
    "rot": (255,0,0),
    "green": (0,255,0),
    "grün": (0,255,0),
    "pink": (230,0,126),
    "off": (0,0,0),
    "aus": (0,0,0)
}

class colourControlClient(discord.Client):
    async def on_ready(self):
        print("Bot connected")
    
    async def on_message(self, message):
        msgContent=message.content
        print(f"{message.author} in \"{message.channel}\": {message.content}")
        colourPayload=None
        if msgContent in colourDict:
            colourPayload={
                "r":colourDict[msgContent][0],
                "g":colourDict[msgContent][1],
                "b":colourDict[msgContent][2]
            }
        # For RGB-values in the following syntax: (r,g,b)
        elif msgContent.startswith("(") and msgContent.endswith(")"):
            rgb=msgContent[1:-1].split(",")
            if len(rgb) == 3:
                colourPayload={
                    "r":rgb[0],
                    "g":rgb[1],
                    "b":rgb[2]
                }
        if colourPayload != None:
            try:
                requests.post(f"http://{serverIP}/colour", params=colourPayload)
            except Exception as e:
                print("An exception accured while connecting to the server")

if __name__ == "__main__":
    client=colourControlClient()
    client.run(discordToken)

from operator import truediv
import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))



client.run(token)
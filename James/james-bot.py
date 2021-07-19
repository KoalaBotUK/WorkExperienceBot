import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

client = commands.Bot(command_prefix='!')

token = os.environ['DISCORD_TOKEN']

@client.event
async def on_ready():
    print("Bot user" +client.user.name+" is ready.")

@client.command()
async def hi(cxt, args):
        if cxt.author == client.user:
            return 
        await cxt.channel.send("Hello "+ args +"!")

#@client.event
#async def on_message(msg):
#    if msg.author == client.user:
#        return                           # Don’t respond to itself
#    if msg.content == "Ping":            # Check that the message content matches
#        await msg.channel.send("Pong!")  # If it does, reply

client.run(token)
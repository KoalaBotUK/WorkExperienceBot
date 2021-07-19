import os
import discord

from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot user {client.user} is ready.")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return                           # Don’t respond to itself
    if msg.content == "Ping":            # Check that the message content matches
        await msg.channel.send("Pong!")  # If it does, reply

load_dotenv()
BOT_TOKEN=os.environ['TOKEN']
client.run(BOT_TOKEN)
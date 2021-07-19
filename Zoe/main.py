import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Bot user {bot.user} is ready.")
    bot.load_extension("cogs.greetings")
    bot.load_extension("cogs.sort")


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if msg.content == "Ping":
        await msg.channel.send("Pong!")

    if msg.content.lower() == "no one calls esteban julio ricardo montoya de la rosa ramírez a thief!":
        await msg.channel.send("NO ONE'S GOT THE TIME")


load_dotenv()
BOT_TOKEN=os.environ['TOKEN']
bot.run(BOT_TOKEN)
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f"Bot user {client.user} is ready.")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content == "Ping":
        await msg.channel.send("Pong!")

    await bot.process_commands(msg)

@bot.command(name="hey")
async def hey(ctx, *, args):
    if args:
        await ctx.send("Hey " + args)
    else:
        await ctx.send("Hey " + ctx.message.author.name)


load_dotenv()
BOT_TOKEN=os.environ['TOKEN']
client.run(BOT_TOKEN)
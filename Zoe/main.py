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
    bot.load_extension("cogs.random")
    bot.load_extension("cogs.twitter")


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    if msg.content == "Ping":
        await msg.channel.send("Pong!")

    if msg.content == "easter":
        await msg.channel.send("egg")

    if msg.content.lower() == "no one calls esteban julio ricardo montoya de la rosa ramírez a thief!":
        await msg.channel.send("NO ONE'S GOT THE TIME")

    await bot.process_commands(msg)


#command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing argument.")


load_dotenv()
BOT_TOKEN=os.environ['TOKEN']
bot.run(BOT_TOKEN)
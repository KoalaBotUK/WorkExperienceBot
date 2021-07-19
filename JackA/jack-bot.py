import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

client = discord.Client()

token = os.environ['DISCORD_TOKEN']
COMMAND_PREFIX = "!"

client = commands.Bot(command_prefix=COMMAND_PREFIX)


@client.event
async def on_ready():
    print(f"Bot user {client.user} is ready.")


@client.command()
async def Ping(ctx):
        await ctx.channel.send("Pong!")  # If it does, reply

@client.command()
async def hi(ctx, arg):
    if ctx.author == client.user:
        return
    await ctx.channel.send("hello " + arg + "!")

@hi.error
async def hi_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("hello " + ctx.author.display_name + "!")

@client.command()
async def sort(ctx, *args):
    if ctx.author == client.user:
        return
    await ctx.send(str(len(args)) + " argument(s)")
    await ctx.send("Sorted arguments: " + ", ".join(sorted(args)))


client.run(token)

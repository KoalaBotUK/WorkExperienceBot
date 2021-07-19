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
async def hi(ctx, args = ""):
        if ctx.author == client.user:
            return 
        if (args == ""):
            print("no args")
            await ctx.channel.send("Hello "+ ctx.author.name +"!")

        else:
            await ctx.channel.send("Hello "+ args +"!")

@client.command()
async def sort(cxt,*args):
        if cxt.author == client.user:
            return 
        else:
            print(list(args))
            argList = list(args)
            sortedArgs = argList.sort()
            await cxt.send('{} arguments: {}'.format(len(argList), ', '.join(argList)))

#@client.event
#async def on_message(msg):
#    if msg.author == client.user:
#        return                           # Don’t respond to itself
#    if msg.content == "Ping":            # Check that the message content matches
#        await msg.channel.send("Pong!")  # If it does, reply

client.run(token)
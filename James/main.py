from inspect import classify_class_attrs
import discord
from argsort import SearchCog
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

client = commands.Bot(command_prefix='!', help_command=None)

token = os.environ['DISCORD_TOKEN']
client.add_cog(SearchCog(client))
search = client.get_cog("SearchCog")
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

#@client.event
#async def on_message(msg):
#    if msg.author == client.user:
#        return                           # Don’t respond to itself
#    if msg.content == "Ping":            # Check that the message content matches
#        await msg.channel.send("Pong!")  # If it does, reply
if __name__ == "__main__":
    client.run(token)
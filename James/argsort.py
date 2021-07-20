import discord
from discord.ext import commands

class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @bot.command()
    async def sort(self, cxt,*args):
        if cxt.author == bot.user:
            return 
        else:
            print(list(args))
            argList = list(args)
            sortedArgs = argList.sort()
            await cxt.send('{} arguments: {}'.format(len(argList), ', '.join(argList)))

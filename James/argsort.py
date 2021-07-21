import discord
from discord.ext import commands

class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sort(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            argList = list(args)
            argList.sort()
            print(('{} arguments: {}'.format(len(argList), ', '.join(argList))))

            await cxt.send('{} arguments: {}'.format(len(argList), ', '.join(argList)))

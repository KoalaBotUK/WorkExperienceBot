import discord
from discord.ext import commands

class Sort(commands.Cog):
    async def sort(ctx, *args):
        argsList = []
        for item in args:
            argsList.append(item)
        argsList.sort()

        output = "{} arguments: ".format(len(args))
        for item in argsList:
            output += item + " "

        await ctx.send(output)

def setup(bot):
    bot.add_cog(Sort(bot))
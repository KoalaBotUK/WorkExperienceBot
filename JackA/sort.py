import discord
from discord.ext import commands


class Sort(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def sort(self, ctx, *args):
        await ctx.send(str(len(args)) + " argument(s)")
        await ctx.send("Sorted arguments: " + ", ".join(sorted(args)))


def setup(bot):
    bot.add_cog(Sort(bot))

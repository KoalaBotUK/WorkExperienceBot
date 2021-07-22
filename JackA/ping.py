import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))

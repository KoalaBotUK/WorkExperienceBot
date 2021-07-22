import discord
from discord.ext import commands


class Hi(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def hi(self, ctx, arg):
        await ctx.channel.send("hello " + arg + "!")

    @commands.command()
    async def hey(self, ctx):
        print("hello " + ctx.author.display_name + "!")
        await ctx.send("hello " + ctx.author.display_name + "!")


def setup(bot):
    bot.add_cog(Hi(bot))

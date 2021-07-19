import discord
from discord.ext import commands


class Hi(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def hi(self, ctx, arg):
        await ctx.channel.send("hello " + arg + "!")

    @hi.error
    async def hi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("hello " + ctx.author.display_name + "!")


def setup(bot):
    bot.add_cog(Hi(bot))

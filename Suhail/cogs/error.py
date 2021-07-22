from inspect import trace
import discord
from discord.ext import commands
import traceback

class Error(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("I only accept numbers smh")
        else:
            traceback.print_exception(type(error), error, error.__traceback__)


def setup(bot):
    bot.add_cog(Error(bot))

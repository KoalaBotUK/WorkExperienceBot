import discord
from discord.ext import commands

class Error(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("I only accept numbers smh")

def setup(bot):
    bot.add_cog(Error(bot))

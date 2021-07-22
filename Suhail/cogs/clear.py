import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, bot): self.bot = bot

    @commands.command()
    async def clear(self, ctx, num: int):
        try:
            await ctx.channel.purge(limit=num)
        except discord.Forbidden:
            await ctx.send("Oops i can't do that rip")
        
def setup(bot):
    bot.add_cog(Clear(bot))
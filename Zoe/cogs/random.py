import discord
from discord.ext import commands

import random

class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx, number=None):
        if number:
            await ctx.send(random.randint(0, int(number)))
        else:
            await ctx.send(random.randint(0, 100))

def setup(bot):
    bot.add_cog(Random(bot))
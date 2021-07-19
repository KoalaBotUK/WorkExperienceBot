import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def hey(ctx, *, name=None):
        if name:
            if name.lower() == "esteban julio ricardo montoya de la rosa ramírez":
                await ctx.send("Hey thief")
            else:
                await ctx.send("Hey " + name + " :)")
        else:
            await ctx.send("Hey " + ctx.message.author.name + " :)")

def setup(bot):
    bot.add_cog(Greetings(bot))
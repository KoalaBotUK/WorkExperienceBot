import aiohttp
import discord
import random
from discord.ext import commands

class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def flip(self, ctx, count: int):
        if count < 0: return await ctx.send("Can't flip a negative number of coins")
        if  count == 0: return await ctx.send("Well... you flipped nothing so... Nothing")
        await ctx.send(" ".join(random.choice(["H", "T"]) for x in range(count)))
    
    @commands.command()
    async def roll(self, ctx, count: int):
        print("HERE")
        if count < 0: return await ctx.send("Can't roll a negative number of dice")
        if count == 0: return await ctx.send("Well... you rolled nothing so... Nothing")
        
        await ctx.send(" ".join(str(random.randint(1, 6)) for x in range(count)))

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                data = await resp.json()
                return await ctx.send(data[0]["url"])

def setup(bot):
    bot.add_cog(Random(bot))
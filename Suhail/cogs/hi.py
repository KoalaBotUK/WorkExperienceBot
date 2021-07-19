import discord
from discord.ext import commands

class Hi(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        return await ctx.send(f"Pong! :ping_pong: Latency: {round(self.bot.latency*1000, 2)}ms")
    
    @commands.command()
    async def hi(self, ctx, name = None):
        name = name or ctx.author.display_name
        await ctx.send(f"hello {name}!")

    @commands.command()
    async def greet(self, ctx):
        await ctx.author.send("Private Greeting oooooooooo")

    @commands.command()
    async def sort(self, ctx, *args):
        await ctx.send("\n".join(sorted(args)))

    @commands.command()
    async def logo(self, ctx):
        await ctx.send(file=discord.File("logo.png"))
    
def setup(bot):
    bot.add_cog(Hi(bot))
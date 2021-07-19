import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    async def on_ready(self):
        print(f"READY! Loaded {self.user}")
        self.load_extension("cogs.hi")
        self.load_extension("cogs.clear")
        self.load_extension("cogs.error")
        self.load_extension("cogs.random")

bot = Bot(command_prefix="!")

bot.run(os.environ["TOKEN"])
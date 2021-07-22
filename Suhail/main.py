import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):

    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        self.load_extension("cogs.hi")
        self.load_extension("cogs.clear")
        self.load_extension("cogs.error")
        self.load_extension("cogs.random")
        self.load_extension("cogs.twitter")

    async def on_ready(self):
        print(f"READY! Loaded {self.user}")
        

bot = Bot(command_prefix="!")

if __name__ == "__main__":
    bot.run(os.environ["TOKEN"])
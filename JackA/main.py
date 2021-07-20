import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

client = discord.Client()

token = os.environ['DISCORD_TOKEN']
COMMAND_PREFIX = "!"

client = commands.Bot(command_prefix=COMMAND_PREFIX)


class Bot(commands.Bot):
    async def on_ready(self):
        print(f"Bot user {client.user} is ready.")


client.load_extension("ping")
client.load_extension("hi")
client.load_extension("sort")

if __name__ == "__main__":
    client.run(token)

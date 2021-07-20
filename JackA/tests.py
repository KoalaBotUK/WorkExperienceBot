import asyncio

import discord
import discord.ext.test as dpytest
import pytest
from discord.ext import commands

import main
import ping
import hi

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True


@pytest.fixture(autouse=True)
def ping_cog(bot: commands.Bot):
    ping_cog = ping.Ping(bot)
    bot.add_cog(ping_cog)
    dpytest.configure(bot)
    return ping_cog


@pytest.fixture(autouse=True)
def bot(event_loop):
    bot = commands.Bot("!", loop=event_loop, intents=intents)
    dpytest.configure(bot)
    print("Starting bot tests")
    return bot


@pytest.mark.asyncio
async def test_ping_returns_pong(bot):
    # send !ping and make sure the bot sends Pong!
    print("test")
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Pong!")



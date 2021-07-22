import asyncio

import discord
import discord.ext.test as dpytest
import pytest
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

import main
import ping
import hi
import sort

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
def hi_cog(bot: commands.Bot):
    hi_cog = hi.Hi(bot)
    bot.add_cog(hi_cog)
    dpytest.configure(bot)
    return hi_cog


@pytest.fixture(autouse=True)
def sort_cog(bot: commands.Bot):
    sort_cog = sort.Sort(bot)
    bot.add_cog(sort_cog)
    dpytest.configure(bot)
    return sort_cog


@pytest.fixture(autouse=True)
def bot(event_loop):
    bot = commands.Bot("!", loop=event_loop, intents=intents)
    dpytest.configure(bot)
    print("Starting bot tests")
    return bot


@pytest.mark.asyncio
async def test_ping_returns_pong(bot):
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Pong!")


@pytest.mark.asyncio
async def test_hi_name_correct_return(bot):
    await dpytest.message("!hi Jack")
    assert dpytest.verify().message().contains().content("hello Jack!")


@pytest.mark.asyncio
async def test_hey_correct_return(bot):
    await dpytest.message("!hey")
    assert dpytest.verify().message().contains().content("hello TestUser0_0_nick!")


@pytest.mark.asyncio
async def test_sort(bot):
    await dpytest.message("!sort e d a c b")
    assert dpytest.verify().message().contains().content("5 argument(s)" + "\n" + "Sorted arguments: a, b, c, d, e")


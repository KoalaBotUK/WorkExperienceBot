import asyncio
import pytest
import discord
from discord.ext import commands, test as dpytest

from cogs import hi
@pytest.fixture
async def bot(event_loop):

    intents = discord.Intents.default()
    intents.members = True

    b = commands.Bot(command_prefix="!", loop=event_loop, intents=intents)
    dpytest.configure(b)
    return b

@pytest.fixture(autouse=True)
def hi_cog(bot: commands.Bot):
    hi_cog = hi.Hi(bot)
    bot.add_cog(hi_cog)
    dpytest.configure(bot)
    return hi_cog


@pytest.mark.asyncio
async def test_hi():
    await dpytest.message("!hi suhail")
    assert dpytest.verify().message().content("hello suhail!")

@pytest.mark.asyncio
async def test_logo():
    await dpytest.message("!logo")
    assert dpytest.verify().message().attachment("logo.png")

@pytest.mark.asyncio
async def test_ping():
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Pong!")


@pytest.mark.parametrize("test_input,expected", [("insist establish arm brown understand", "arm\nbrown\nestablish\ninsist\nunderstand"), ("tension issue breakdown claim old", "breakdown\nclaim\nissue\nold\ntension")])
@pytest.mark.asyncio
async def test_sort(test_input, expected):
    await dpytest.message(f"!sort {test_input}")
    assert dpytest.verify().message().content(expected)

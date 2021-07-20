import asyncio
import pytest
import discord.ext.test as dpytest
import discord.ext.commands as commands

from cogs import greetings

@pytest.fixture
async def bot(event_loop):
    b = commands.Bot("!", loop=event_loop)
    dpytest.configure(b)
    return b

@pytest.fixture(autouse=True)
def greetings_cog(bot: commands.Bot):
    greetings_cog = greetings.greetings(bot)
    bot.add_cog(greetings_cog)
    dpytest.configure(bot)
    return greetings_cog

@pytest.mark.asyncio
async def test_with_name():
    await dpytest.message("!hey abluey")
    assert dpytest.verify().message().content("Hey abluey :)")
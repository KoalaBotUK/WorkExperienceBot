import asyncio
import pytest
import discord
import discord.ext.test as dpytest
import discord.ext.commands as commands

from cogs import greetings

@pytest.fixture(autouse=True)
async def bot(event_loop):
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    b = commands.Bot("!", loop=event_loop, intents=intents)
    dpytest.configure(b)
    return b

@pytest.fixture(autouse=True)
def greetings_cog(bot: commands.Bot):
    greetings_cog = greetings.Greetings(bot)
    bot.add_cog(greetings_cog)
    dpytest.configure(bot)
    return greetings_cog

@pytest.mark.asyncio
async def test_with_name():
    await dpytest.message("!hey john")
    assert dpytest.verify().message().content("Hey john :)")

@pytest.mark.asyncio
async def test_without_name():
    await dpytest.message("!hey")
    assert dpytest.verify().message().content("Hey TestUser0 :)")
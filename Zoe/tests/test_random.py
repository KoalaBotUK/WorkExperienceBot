import asyncio
import pytest
import discord
import discord.ext.test as dpytest
import discord.ext.commands as commands

from cogs import random

@pytest.fixture(autouse=True)
async def bot(event_loop):
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    b = commands.Bot("!", loop=event_loop, intents=intents)
    dpytest.configure(b)
    await dpytest.empty_queue()
    return b

@pytest.fixture(autouse=True)
def random_cog(bot: commands.Bot):
    random_cog = random.Random(bot)
    bot.add_cog(random_cog)
    dpytest.configure(bot)
    return random_cog

@pytest.mark.asyncio
async def test_with_param():
    await dpytest.message("!random 0")
    assert dpytest.verify().message().content("0")

@pytest.mark.asyncio
async def test_without_param():
    await dpytest.message("!random")
    msg = dpytest.sent_queue.peek()
    assert int(msg.content) <= 100
import asyncio
import pytest
import discord
import discord.ext.test as dpytest
import discord.ext.commands as commands

from cogs import sort

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
def sort_cog(bot: commands.Bot):
    sort_cog = sort.Sort(bot)
    bot.add_cog(sort_cog)
    dpytest.configure(bot)
    return sort_cog

@pytest.mark.asyncio
async def test_sort():
    await dpytest.message("!sort house dog")
    msg = dpytest.sent_queue.peek()
    assert dpytest.verify().message().content("2 arguments: dog house"), msg.content

@pytest.mark.asyncio
async def test_sort_no_params():
    await dpytest.message("!sort")
    assert dpytest.verify().message().content("No arguments found.")
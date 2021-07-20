import discord.ext.test as dpytest
import discord
import pytest
from discord.ext import commands

import main

@pytest.fixture(autouse=True)
async def initalBot(event_loop):
    print("Tests starting")
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    bot = commands.Bot("!", intents)
    for com in main.client.commands:
        if com.name != "help":
            bot.add_command(com)
    await dpytest.empty_queue()
    dpytest.configure(bot)
    print("Starting bot tests")
    return bot


@pytest.mark.asyncio
async def test_default_hi():
    await dpytest.message("!hi")
    assert dpytest.verify.message.content("Hello james!")
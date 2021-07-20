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
    tBot = commands.Bot("!", intents)
    for com in main.client.commands:
        if com.name != "help_command" and com.name != "help":
            tBot.add_command(com)
    await dpytest.empty_queue()
    dpytest.configure(tBot)
    print("Starting bot tests")
    return tBot


@pytest.mark.asyncio
async def test_default_hi():
    await dpytest.message("!hi")
    assert dpytest.verify.message.content("Hello james!")
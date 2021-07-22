import os

import discord
import requests
from discord.ext import commands


class Twitter(commands.Cog):
    def __init__(self, client):
        self.bot = client

    def bearer_oauth(self, r):
        bearer_token = os.environ.get("BEARER_TOKEN")
        r.headers["Authorization"] = f"Bearer {bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r

    @commands.command()
    async def latest_tweet(self, ctx, arg):
        query_params = {'query': '(from:'+arg+' -is:retweet)', 'tweet.fields': 'author_id', 'max_results' : 10}
        url = "https://api.twitter.com/2/tweets/search/recent"
        tweets = requests.get(url, auth=self.bearer_oauth, params=query_params)
        await ctx.channel.send(arg + "'s latest tweet: \n" + tweets.json()['data'][0]['text'])

    @commands.command()
    async def tweet(self, ctx, *args):
        await ctx.channel.send("Pong!")


def setup(bot):
    bot.add_cog(Twitter(bot))

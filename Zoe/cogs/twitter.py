import os
import requests
import json

import discord
from discord.ext import commands

class Twitter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.apiKey = os.environ['KOALA_API_KEY']
        self.apiSecret = os.environ['KOALA_SECRET_KEY']
        self.accessToken = os.environ['KOALA_ACCESS']
        self.accessSecret = os.environ['KOALA_ACCESS_SECRET']
        self.bearerToken = os.environ['KOALA_BEARER']

    # def create_url():
    #     return "https://api.twitter.com/2/users/1415763208477020163/tweets"

    # def get_params():
    #     return {"tweets.fields":"created_at"}

    def bearer_oauth(self, r):
        r.headers["Authorization"] = f"Bearer {self.bearerToken}"
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r

    @commands.command()
    async def get_tweet(self, ctx, user):

        try:
            userIDResponse = requests.request("GET", "https://api.twitter.com/2/users/by/username/{}".format(user), auth=self.bearer_oauth, params="")
            userResponseJson = userIDResponse.json()
            userID = userResponseJson["data"]["id"]

            response = requests.request("GET", "https://api.twitter.com/2/users/{}/tweets".format(userID), auth=self.bearer_oauth, params="")
            json_response = response.json()

            url = "https://twitter.com/i/web/status/{}".format(json_response["data"][0]["id"])
            description = json_response["data"][0]["text"]

            username = userResponseJson["data"]["username"]

            embed = discord.Embed(title="{}'s last tweet".format(username), description=description, url=url)

            await ctx.send(embed=embed)

        except:
            await ctx.send(":(")


def setup(bot):
    bot.add_cog(Twitter(bot))
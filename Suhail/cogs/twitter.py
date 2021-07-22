import aiohttp
import os
from dateutil import parser
import discord
from discord.ext import commands

class Twitter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ["TWITTER_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
    
    @commands.group(invoke_without_command=True)
    async def twitter(self, ctx: commands.Context):
        return await ctx.send_help("twitter")
    
    @twitter.command()
    async def lasttweet(self, ctx, username: str):
        tdata, error = await self.get_user_by_name(username)
        if error:
            return await ctx.send(tdata["errors"][0]["detail"])
        tweet, metrics, timestamp = await self.get_latest_tweet(tdata["data"]["id"])

        timestamp = parser.parse(timestamp)

        embed = discord.Embed(
            title=f"{username}'s last tweet",
            description = tweet,
            color=0x00ff00,
            timestamp = timestamp,
        )

        embed.add_field(name="Likes", value=metrics["like_count"])
        embed.add_field(name="RTs", value=metrics["retweet_count"])
        embed.add_field(name="Quote Tweets", value=metrics["quote_count"])
        embed.add_field(name="Replies", value=metrics["reply_count"])

        embed.set_footer(text="Created at")


        await ctx.send(embed=embed)

    @twitter.command()
    async def userinfo(self, ctx, username: str):

        tdata, error = await self.get_user_by_name(username)
        if error:
            return await ctx.send(tdata["errors"][0]["detail"])
        
        embed = discord.Embed(
            title=f"@{username}",
            timestamp = parser.parse(tdata["data"]["created_at"]),
            color = 0x00ff00
        )
        embed.add_field(name="Name",value=tdata["data"]["name"], inline=False)
        embed.add_field(name="Bio",value=tdata["data"]["description"], inline=False)
        embed.add_field(name="Followers", value=tdata["data"]["public_metrics"]["followers_count"])
        embed.add_field(name="Following", value=tdata["data"]["public_metrics"]["following_count"])
        embed.add_field(name="Tweets", value=tdata["data"]["public_metrics"]["tweet_count"])
        embed.set_footer(text="Created at")
        embed.set_thumbnail(url=tdata["data"]["profile_image_url"])

        await ctx.send(embed=embed)
    

    async def get_user_by_name(self, username: str):
        url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=created_at,name,description,public_metrics,profile_image_url"
        
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(url, headers=self.headers) as resp:
                data = await resp.json()
        
        return data, "errors" in data
    
    async def get_latest_tweet(self, tid: str):
        url = f"https://api.twitter.com/2/users/{tid}/tweets?tweet.fields=public_metrics,created_at,text"

        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(url, headers=self.headers) as resp:
                data = await resp.json()

        last_tweet = data["meta"]["newest_id"]
        tweet = [x for x in data["data"] if x["id"] == last_tweet]

        return tweet[0]["text"], tweet[0]["public_metrics"], tweet[0]["created_at"]
            


def setup(bot):
    bot.add_cog(Twitter(bot))
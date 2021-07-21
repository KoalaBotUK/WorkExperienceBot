import sqlite3
import discord
from discord.ext import commands


class InventoryManager(commands.Cog):
    def __init__(self, client):
        self.bot = client

    con = sqlite3.connect('Inventory.db')
    cur = con.cursor()
    #cur.execute('''CREATE TABLE inventory
     #              (item_id INTEGER, count INTEGER, society_id INTEGER)''')
    #cur.execute('''CREATE TABLE removedItems
     #              (item_id INTEGER, count_removed INTEGER, date_removed DATE DEFAULT current_date , user_id INTEGER, society_id INTEGER)''')
    #cur.execute('''CREATE TABLE users
     #              (user_id INTEGER AUTO_INCREMENT, user_name TEXT, society_id INTEGER)''')
    #cur.execute('''CREATE TABLE societies
     #              (society_id INTEGER AUTO_INCREMENT, society_name TEXT, server_id INTEGER, role_id INTEGER)''')
    #cur.execute('''CREATE TABLE items
     #              (item_id INTEGER AUTO_INCREMENT, item_name TEXT, item_description TEXT)''')

    @commands.command()
    async def take(self, ctx, item_id, count, society_id):
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        # Decrease the count in the inventory table for item_id and society_id by count
        # If count = 0, remove item from table
        cur.execute('''INSERT INTO removedItems (item_id, count, date_removed, user_id, society_id) VALUES (item_id, count, current_date, user_id, society_id)''')

    @commands.command()
    async def return_item(self, ctx, item_id, count, society_id):
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        # Increase the count in the inventory table for item_id and society_id by count
        # If count was 0, add item to table
        cur.execute('''INSERT INTO inventory (item_id, count, society_id) VALUES (item_id, count, society_id)''')

    @commands.command()
    async def view_inventory(self, ctx):
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM inventory")
        await ctx.channel.send(cur.fetchall())

    @commands.command()
    async def view_removed(self, ctx, society_id):
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM removed WHERE society_id==society_id")
        await ctx.channel.send(cur.fetchall())


def setup(bot):
    bot.add_cog(InventoryManager(bot))

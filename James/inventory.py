import sqlite3
import discord
from discord.ext import commands
import datetime


# for reference :)
# import datetime
# f"{datetime.datetime.now():%d-%m-%Y}"
# outputs date in dd-mm-YYYY


class InventoryCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.con = sqlite3.connect('inventory.db')
        self.cur = self.con.cursor()

        # Create tables
        cur.executescript('''CREATE TABLE Items (
                            ItemID integer AUTO_INCREMENT,
                            ItemName varchar(255),
                            ItemDescription varchar(255),
                            Amount integer,
                            PRIMARY KEY (ItemID)
                        );
                        
                        CREATE TABLE Checkout (
                            CheckoutID varchar(255),
                            User varchar(255),
                            TakenAmount integer,
                            TakenDate datetime,
                            ItemID integer,
                            PRIMARY KEY (CheckoutID),
                            FOREIGN KEY (ItemID)
                        );'''
                    )

        # Inserting values into ITEMS
        cur.executescript('''INSERT INTO Items (ItemID, ItemName, ItemDesc, Amount) VALUES
                                (1, "Headphones", "Pair of headphones", 10);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Mice", "Mice not sure what you expect", 5);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Keyboard", "Goes click click click", 6);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Computer", "Has input + output and sometimes runs", 10);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Mousemat", "Flat thing to put mouse on", 4);''')

        # Inserting values into CHECKOUT
        cur.executescript('''INSERT INTO Checkout (CheckoutID, User, TakenAmount, TakenDate) VALUES
                                ("C1", )''')
    

    #Checkout item (almost completed)
    '''
    Arg 1: item id
    Arg 2: amount
    '''
    @commands.command()
    async def checkout(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            amount = args[1]
            itemId = args[0]
            #Find the total checked out for the item
            checkedOut = self.cur.execute('SELECT Sum(TakenAmount) FROM Checkout WHERE (?)', (itemId))
            #Should check to see if the item exists
            total = self.cur.execute('SELECT Amount FROM Items WHERE (?)', (itemId))
            if(checkedOut + amount < total):
                checkedOut = self.cur.execute('INSERT INTO Checkout (?,?,?,?,?)', (checkID, cxt.author, amount, date, itemId)) # 1st and 4th should be autocreated
                await cxt.send("User "+ cxt.author + " successfully checked out " + amount + " of item " + itemId)
            else:
                await cxt.send("The guild doesn't currently have that item availible")


    #Return item
    @commands.command()
    async def return_item(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            if(userCheckedOutItem):
                await cxt.send("")
            else:
                await cxt.send("")




    #View checked out items (completed)
    @commands.command()
    async def view_checkouts(self, cxt):
        if cxt.author == self.bot.user:
            return 
        else:
            allCheckedOut = self.cur.execute('SELECT * FROM Checkout')
            for row in allCheckedOut:
                await cxt.send(row)

    #View instock  (have to loop through all checkouts)
    @commands.command()
    async def view_stock(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            argList = list(args)
            argList.sort()
            print(('{} arguments: {}'.format(len(argList), ', '.join(argList))))

            await cxt.send('{} arguments: {}'.format(len(argList), ', '.join(argList)))

    #Search society items 
    @commands.command()
    async def search(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            searchString - args[0]
            result = self.cur.execute('SELECT * FROM Items WHERE (?)', (searchString))
            await cxt.send("")


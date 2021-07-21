import sqlite3
import discord
from discord.ext import commands
import datetime


# for reference :)
# import datetime
# datetime.datetime.now().strftime("%d-%m-%Y")
# outputs date in dd-mm-YYYY, a string


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
                            CheckoutID integer AUTO_INCREMENT,
                            User varchar(255),
                            TakenAmount integer,
                            TakenDate varchar(10),
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
        cur.executescript('''INSERT INTO Checkout (CheckoutID, User, TakenAmount, TakenDate, ItemID) VALUES
                                ("1", "A", 2, "14-07-21", 1);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("B", 8, "14-07-21", 1);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("B", 2, "13-07-21", 2);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("D", 1, "14-07-21", 2);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("A", 3, "14-07-21", 3);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("C", 6, "13-07-21", 4);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("A", 1, "14-07-21", 4);
                            INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ("D", 4, "14-07-21", 5);
                        ''')
    

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
            itemId = args[0]
            amount = args[1]
            #Find the total checked out for the item
            #checkedOut = self.cur.execute('SELECT Sum(TakenAmount) FROM Checkout WHERE ItemID = (?)', (itemId))
            #Should check to see if the item exists
            total = self.cur.execute('SELECT Amount FROM Items WHERE ItemID = (?)', (itemId))
            if(amount <= total):
                checkedOut = self.cur.execute('''INSERT INTO Checkout (User, TakenAmount,ItemID)
                (?,?,?)
                ''', (cxt.message.author.id, amount, itemId))
                checkedOut = self.cur.execute('''INSERT INTO Checkout (User, TakenAmount,ItemID)(?,?,?)''', (cxt.message.author.id, amount, itemId))
                await cxt.send("User "+ cxt.author + " successfully checked out " + amount + " of item " + itemId)
            else:
                await cxt.send("The guild doesn't currently have that item availible")


    #Return item
    @commands.command()
    async def return_item(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            itemId = args[0]
            amounts = args[1]
            
            takenAmount = self.cur.execute('SELECT TakenAmount FROM Checkout WHERE User = (?)', (cxt.message.author.id))




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
            result = self.cur.execute('SELECT * FROM Items WHERE ItemName = (?)', (searchString))
            await cxt.send("")


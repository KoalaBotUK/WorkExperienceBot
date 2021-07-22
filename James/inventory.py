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
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Items (
                            ItemID integer PRIMARY KEY AUTOINCREMENT,
                            ItemName varchar(255),
                            ItemDesc varchar(255),
                            Amount integer
                        );'''
                    )


        self.cur.execute('''CREATE TABLE IF NOT EXISTS Checkout (
                            CheckoutID integer PRIMARY KEY AUTOINCREMENT,
                            User varchar(255),
                            TakenAmount integer,
                            TakenDate varchar(10),
                            ItemID integer,
                            CONSTRAINT fk_extensions
                            FOREIGN KEY (ItemID)
                            REFERENCES Items (ItemID)
                        );'''
                    )
        self.con.commit()

        # Inserting values into ITEMS
        print("inserting items")
        self.cur.executescript('''INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ( "Headphones", "Pair of headphones", 10);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Mice", "Mice not sure what you expect", 5);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Keyboard", "Goes click click click", 6);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Computer", "Has input + output and sometimes runs", 10);
                            INSERT INTO Items (ItemName, ItemDesc, Amount) VALUES
                                ("Mousemat", "Flat thing to put mouse on", 4);''')
        self.con.commit()

        print("commited items")

        # Inserting values into CHECKOUT
        print("inserting checkouts")
        self.cur.executescript('''INSERT INTO Checkout (User, TakenAmount, TakenDate, ItemID) VALUES
                                ( "A", 2, "14-07-21", 1);
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

        self.con.commit()

        print("commited checkouts")
    

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
            itemId = int(args[0])
            amount = int(args[1])

            #Should check to see if the item exists
            total = self.cur.execute('SELECT Amount FROM Items WHERE ItemID = (?)', (str(itemId)))
            
            #Check to see if the item exists
            if self.cur.fetchone() == None:
                await cxt.send("The guild doesn't currently have that item")
                
            elif (amount <= total):
                checkedOut = self.cur.execute('''INSERT INTO Checkout (User, TakenAmount,ItemID)
                (?,?,?)
                ''', (cxt.message.author.id, amount, str(itemId)))
                updateAmount = self.cur.execute('''UPDATE Items 
                SET Amount = (?)
                WHERE ItemID = (?)''', (total - amount, str(itemId)))

                self.con.commit()
                
                await cxt.send("User "+ cxt.author + " successfully checked out " + amount + " of item " + str(itemId))

            elif (0 > amount):
                await cxt.send("You're trying to checkout negative items?!")
                
            else:
                await cxt.send("The guild doesn't currently have that item in stock")


    # SHOULD work???
    #Return item
    @commands.command()
    async def return_item(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            itemId = int(args[0])
            amount = int(args[1])
            
            # Gets the CheckoutID and amount that was checked out
            checkoutId = self.cur.execute('SELECT CheckoutID FROM Checkout WHERE User = (?) AND ItemID = (?)', (cxt.message.author.id, str(itemId)))
            takenAmount = self.cur.execute('SELECT TakenAmount FROM Checkout WHERE User = (?)', (cxt.message.author.id))

            if (amount == 0):
                await cxt.send("Why are you returning 0 items? Is this a joke?")

            # user is returning something
            else:
                if (takenAmount == amount):
                    self.cur.execute('DELETE FROM Checkout WHERE CheckoutID = (?)', (checkoutId))
                    self.con.commit()
                    await cxt.send("All items returned. Checkout entry {0} deleted from table.".format(checkoutId))

                elif (0 < takenAmount < amount):
                    self.cur.execute('UPDATE Checkout SET TakenAmount = (?) WHERE CheckoutID = (?)', (takenAmount - amount), (checkoutId))
                    self.con.commit()
                    await cxt.send("Some items returned. Checkout entry {0} updated.".format(checkoutId))
                
                # if user is returning a negative value 
                else:
                    await cxt.send("If you want to borrow more items, please use !checkout.")



    #View checked out items (completed)
    @commands.command()
    async def view_checkouts(self, cxt):
        if cxt.author == self.bot.user:
            return 
        else:
            allCheckedOut = self.cur.execute('SELECT * FROM Checkout')
            for row in allCheckedOut:
                await cxt.send(row)


    #View instock
    @commands.command()
    async def view_stock(self, cxt,*args):
        if cxt.author == self.bot.user:
            return
        else:
            inStock = self.cur.execute('SELECT * FROM Items WHERE Amount != 0')
            for row in inStock:
                await cxt.send(row)


    #Search society items 
    @commands.command()
    async def search(self, cxt,*args):
        if cxt.author == self.bot.user:
            return 
        else:
            searchString = args[0]
            result = self.cur.execute('SELECT * FROM Items WHERE ItemName = (?)', (searchString))
            if (self.cur.fetchone() == None):
                await cxt.send("The guild does not have an item with that name")
            else:
                for row in result:
                    await cxt.send(row)

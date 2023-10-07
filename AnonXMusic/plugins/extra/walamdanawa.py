import asyncio


import random
from AnonXMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

           "**هەردەم پێبکەنە ♥️😻**",


             "😂😂😂😂😂😂😂",
            
            
            "**پیبکانا پیبکانە هەر دەم بە زەردەخەنە 😂😂**",
            
            
            "**بمێنی♥️😻**",


             "**هەموو کات زەردەخەنە😂😂**",
            

            "**احح لەو پیکنینە 😂😂**",
            
           
 
            
            

        ]


        


@app.on_message(command(["ههه","😂😂","😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))

async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")

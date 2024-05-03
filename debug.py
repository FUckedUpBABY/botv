from pyrogram import Client 
import json

plugins = dict(root="BOT")

with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)
    API_ID = DATA["API_ID"]
    API_HASH = DATA["API_HASH"]
    BOT_TOKEN = DATA["DEBUG_BOT"]

user = Client( 
            "Scrapper", 
             api_id=API_ID, 
             api_hash=API_HASH
              )

bot = Client(
    "DEBUG_BOT", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN, 
    plugins=plugins 
)



if __name__ == "__main__":
    print("Done Bot Active ✅")
    print("NOW START BOT ONCE MY MASTER")

    bot.run()

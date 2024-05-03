import traceback
from pyrogram import Client, filters
from FUNC.usersdb_func import *
import asyncio
from mongodb import client, folder
import json
from pathlib import Path
import time


@Client.on_message(filters.command("export", [".", "/"]))
async def stats(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            msg1 = await message.reply_text(resp, message.id)
        else:
            start = time.time()
            resp = "<b>EXPORTING TEST DATABASE...</b>"
            delete = await message.reply_text(resp, message.id)
            users_db = folder.USERSDB
            chats_auth_db = folder.CHATS_AUTH
            gc_db = folder.GCDB

            all_users = users_db.find({}, {"_id": 0})
            chats = chats_auth_db.find({}, {"_id": 0})
            gcdb = gc_db.find({}, {"_id": 0})

            # EXPORTING ALL USER DATA
            user = 0
            ALL_USERS = ""
            user_amt = 0
            for i in all_users:
                user_amt += 1
                data = json.dumps(i)
                ALL_USERS += f"{data}\n"
                user += 1
            with open("TEST_USERS_DB.json", "a") as f:
                f.write(f"{ALL_USERS}")
            caption = f"""<b>
SUCCESSFULLY RETRIEVED USERS DATABASE ✅

Total Users: {user_amt}
Data Type: JSON
Last Updated: a while ago
Requested Time: {message.date}
  </b>"""
            send = await message.reply_document(
                document="TEST_USERS_DB.json",
                caption=caption,
                reply_to_message_id=message.id,
            )
            if send:
                name = "TEST_USERS_DB.json"
                my_file = Path(name)
                my_file.unlink()

            # EXPORTING ALL APPROVED CHATS DATA
            chat = 0
            ALL_CHATS = ""
            chats_amt = 0
            for i in chats:
                chats_amt += 1
                data = json.dumps(i)
                ALL_CHATS += f"{data}\n"
                chat += 1
            with open("TEST_CHATS_DB.json", "a") as f:
                f.write(f"{ALL_CHATS}")
            caption = f"""<b>
SUCCESSFULLY RETRIEVED CHATS AUTH DATABASE ✅

Total Chats: {chats_amt}
Data Type: JSON
Last Updated: a while ago
Requested Time: {message.date}
  </b>"""
            send = await message.reply_document(
                document="TEST_CHATS_DB.json",
                caption=caption,
                reply_to_message_id=message.id,
            )
            if send:
                name = "TEST_CHATS_DB.json"
                my_file = Path(name)
                my_file.unlink()

            # EXPORTING ALL GC DATA
            gc = 0
            ALL_GC = ""
            gc_amt = 0
            for i in gcdb:
                gc_amt += 1
                data = json.dumps(i)
                ALL_GC += f"{data}\n"
                gc += 1
            with open("TEST_GC_DB.json", "a") as f:
                f.write(f"{ALL_GC}")
            caption = f"""<b>
SUCCESSFULLY RETRIEVED GIFTCARDS DATABASE ✅

Total GC: {gc_amt}
Data Type: JSON
Last Updated: a while ago
Requested Time: {message.date}
  </b>"""
            send = await message.reply_document(
                document="TEST_GC_DB.json",
                caption=caption,
                reply_to_message_id=message.id,
            )
            if send:
                name = "TEST_GC_DB.json"
                my_file = Path(name)
                my_file.unlink()
            await Client.delete_messages(message.chat.id, delete.id)
            end = time.time()
            finalresp = f"""<b>
EXPORT DONE ✅

1. USERS DATABASE ( {user_amt} )
2. CHATS AUTH DATABASE ( {chats_amt} )
3. GIFTCARDS DATABASE ( {gc_amt} )

Data Type: JSON
Last Updated: a while ago
Time Taken: {end - start:0.1f}s
Requested Time: {message.date} </b>
            """
            await message.reply_text(finalresp, message.id)

    except Exception as e:
        await message.reply_text(e, message.id)

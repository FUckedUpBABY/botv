from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("gethits", [".", "/"]))
async def cmd_buy(Client, message):
    try:
        user_id = str(message.from_user.id)
        key = message.text.split(" ")[1]
        file = f"HITS/{key}.txt"
        text = f"""<b>HITS File Successfully Retrieved ✅

Your User ID : {user_id}
Hits Key : {key}

Status : Successfull</b>"""
        await message.reply_document(
            document=file,
            caption=text,
            reply_to_message_id=message.id
                                                )
    except Exception:
        await message.reply_text(f"""<b>File Fetched Failed ❌

Reason : Invalid or Incorrect Secret Key</b>""",
                                 message.id)


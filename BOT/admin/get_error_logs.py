import json , os
from pyrogram import Client, filters
from FUNC.defs import *


@Client.on_message(filters.command("geterror", [".", "/"]))
async def cmd_geterror(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        delete         = await message.reply_text("<b>Getting Error Logs...</b>", message.id)

        document = "error_logs.txt"
        await message.reply_document(document = document,  reply_to_message_id = message.id)
        os.remove(document)

        document = "result_logs.txt"
        await message.reply_document(document=document, reply_to_message_id=message.id)
        os.remove(document)

        await Client.delete_messages(message.chat.id, delete.id)

    except:
        import traceback
        await error_log(traceback.format_exc())

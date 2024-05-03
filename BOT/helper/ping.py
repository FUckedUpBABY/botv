from FUNC.defs import *
from pyrogram import Client, filters
import time


@Client.on_message(filters.command("ping", [".", "/"]))
async def cmd_ping(Client, message):
    try:
        start = time.perf_counter()
        resp = "<b>Checking Mahico Checker ⚡ Ping..."
        edit = await message.reply_text(resp, message.id)
        end = time.perf_counter()
        textb = f"""<b>
Bot Name: Mahico CHECKER ⚡ 
Bot Status: Running ✅ 
Ping: {(end-start)*1000:.2f}ms
   </b> """
        await Client.edit_message_text(message.chat.id, edit.id, textb)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())

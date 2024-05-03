import traceback, json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *

@Client.on_message(filters.command("viewsk", [".", "/"]))
async def viewsk(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]

        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️
            
Message: To perform this action, you need admin level power. 
            
Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        sks = await getallsk()
        amt_sk = 0
        sk_text = ""

        for sk in sks:
            amt_sk += 1
            sk_text += f"{amt_sk}. SK: {sk['id']}, PK: {sk['public_key']}\n"

        resp = f"""<b>
Current SK and PK Keys Retrieved Successfully ✅
━━━━━━━━━━━━━━ 
{sk_text}

Total SK Amount: {len(sks)}
        </b>"""

        await message.reply_text(resp, message.id)

    except Exception as e:
        await message.reply_text(str(e), message.id)
        await error_log(traceback.format_exc())

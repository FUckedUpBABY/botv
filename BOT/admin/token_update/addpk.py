import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


@Client.on_message(filters.command("addpk", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return
        
        await addsk(message.reply_to_message.text)
        resp = f"""<b>
pk Key ( Stripe Key ) Successfully Added ✅
━━━━━━━━━━━━━━
{message.reply_to_message.text}

Status: Successfull
    </b>"""
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
        
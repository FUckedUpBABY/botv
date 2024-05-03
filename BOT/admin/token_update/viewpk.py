import traceback, json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


@Client.on_message(filters.command("viewpk", [".", "/"]))
async def viewpk(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        pks     = await getallpk()
        amt_pk  = 0
        pk_text = ""

        for pk in pks:
            amt_pk += 1
            pk_text += f"{amt_pk}.{pk}\n"
        resp = f"""<b>
Current pk Keys Retrieved Successfully ✅
━━━━━━━━━━━━━━ 
{pk_text}

Total pk Amount : {len(pks)}
        </b>"""

        await message.reply_text(resp, message.id)

    except Exception as e:
        await message.reply_text(e, message.id)
        await error_log(traceback.format_exc())
        
import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("cs", [".", "/"]))
async def cmd_cs(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        user_id, module, value = message.text.split(" ")
        await updateuserinfo(user_id, module, value)

        resp = f"""<b>
Custom Info Changed ✅
━━━━━━━━━━━━━━
User_ID : {user_id}
Key_Name : {module}
Key_Value : {value}

Status: Successfull
</b> """
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await message.reply_text(e, message.id)
        await error_log(traceback.format_exc())

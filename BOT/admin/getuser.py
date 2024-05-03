import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("get", [".", "/"]))
async def cmd_add(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        info = await getuserinfo(message.text.split(" ")[1])
        status, plan, expiry, credit, totalkey, reg_at = (
            info["status"],
            info["plan"],
            info["expiry"],
            info["credit"],
            info["totalkey"],
            info["reg_at"],
        )
        send_info = f"""<b>
<b>{message.text.split(" ")[1]}</b> Info on TEST Checker ⚡
━━━━━━━━━━━━━━
● ID: <code>{message.text.split(" ")[1]}</code>
● Profile Link: <a href="tg://user?id={message.text.split(" ")[1]}">Profile Link</a>
● Status: {status}
● Credit: {credit}
● Plan: {plan}
● Plan Expiry: {expiry}
● Key Redeemed : {totalkey}
● Registered at: {reg_at}</b>
"""
        await message.reply_text(send_info, message.id)

    except Exception as e:
        import traceback
        await message.reply_text(str(e), message.id)
        await error_log(traceback.format_exc())

import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("ac", [".", "/"]))
async def cmd_ac(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        try:
            msg = message.text.split(" ")
            amt, user_id = int(msg[1]), msg[2]
            get_info = await getuserinfo(user_id)
            previous_credit = int(get_info["credit"])
            if previous_credit < 0:
                value = amt
            else:
                value = previous_credit + amt
            await directcredit(user_id, value)

            resp = f"""<b>
Credit Added Successfully ✅ 
━━━━━━━━━━━━━━
Amount : {amt}
User ID: <a href="tg://user?id={user_id}">{user_id}</a> 
Previous Credit: {previous_credit} 
After Credit: {value} 

Message: Credit Added to this User Successfully.
    </b>"""
            await message.reply_text(resp, message.id)

        except Exception as e:
            await message.reply_text(e, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())

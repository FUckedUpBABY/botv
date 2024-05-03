import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("pm", [".", "/"]))
async def cmd_pm(Client, message):
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
            user_id = str(message.text.split(" ")[1])
        except:
            user_id = message.reply_to_message.from_user.id

        pm_chk = await getuserinfo(user_id)
        status = str(pm_chk["status"])

        if status != "FREE":
            resp = f"""<b>
Already Promoted ⚠️

User ID: <a href="tg://user?id={user_id}">{user_id}</a> 
Status: Premium

Message: This user is already Premium User . No Need To Promote Again .
    </b> """
            await message.reply_text(resp, message.id)

        else:
            await premiumuser(user_id)
            resp = f"""<b>
Premium Activated Successfully ✅ 
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Role :  Premium

Status : Successfull
    </b> """
            await message.reply_text(resp, message.id)

            user_resp = f"""<b>
Account Promoted Successfully ✅ 
━━━━━━━━━━━━━━ 
User ID: {user_id} 
Role: Premium 

Message: Congratz ! Your Account Successfully Promoted To "Premium" User . Enjoy Yourself on the Bot .
    </b> """
            await Client.send_message(user_id, user_resp)

    except Exception as e:
        import traceback
        await message.reply_text(e, message.id)
        await error_log(traceback.format_exc())

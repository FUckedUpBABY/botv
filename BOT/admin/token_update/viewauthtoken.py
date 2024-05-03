import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *
from CONFIG_DB import *


async def get_auth_token():
    try:
        TOKEN_NAME = "AUTH_TOKEN"
        FIND_TOKEN = TOKEN_DB.find_one({"id": TOKEN_NAME}, {"_id": 0})

        if str(FIND_TOKEN) == "None":
            INFO = {
                "id": TOKEN_NAME,
                "token": "N/A",
                "status": "N/A",
            }
            TOKEN_DB.insert_one(INFO)
            return "N/A"

        else:
            return FIND_TOKEN["token"]
    except:
        import traceback
        await error_log(traceback.format_exc())
        return "N/A"


@Client.on_message(filters.command("viewauthtoken", [".", "/"]))
async def viewauthtoken(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        token = await get_auth_token()
        resp = f"""<b>
Current Auth Token Retrieved Successfully ✅
━━━━━━━━━━━━━━ 
{token}
    </b>"""
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await message.reply_text(e, message.id)
        await error_log(traceback.format_exc())

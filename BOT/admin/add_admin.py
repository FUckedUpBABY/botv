import traceback
import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

@Client.on_message(filters.command("admin", [".", "/"]))
async def cmd_add(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r").read())["OWNER_ID"]

        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: To perform this action, you need admin level power. 

Contact @stripe_xD for more info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        else:
            try:
                user_id = str(message.text.split(" ")[1])
            except:
                return

            with open("FILES/admin.json", "r", encoding="utf-8") as json_file:
                admins_data = json.load(json_file)

            if user_id in admins_data["admins"]:
                resp = f"""<b>
Already Admin ⚠️

ID: {user_id}

Message: This person (<code>{user_id}</code>) is already an admin.
       </b> """
                await message.reply_text(resp, message.id)
            else:
                admins_data["admins"].append(user_id)

                with open("FILES/admin.json", "w", encoding="utf-8") as json_file:
                    json.dump(admins_data, json_file, ensure_ascii=False, indent=4)

                resp = f"""<b>
Admin Added ✅

ID: {user_id}

Message: This person (<code>{user_id}</code>) is successfully added to the admin list.
       </b> """
                await message.reply_text(resp, message.id)

    except Exception as e:
        await message.reply_text(str(e), message.id)
        await error_log(traceback.format_exc())

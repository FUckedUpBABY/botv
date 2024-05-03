import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("add", [".", "/"]))
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

        else:
            try:
                chat_id = str(message.text.split(" ")[1])
            except:
                chat_id = str(message.chat.id)

            getchat = await getchatinfo(chat_id)
            getchat = str(getchat)
            
            if getchat == "None":
                await addchat(chat_id)
                resp = f"""<b>
Group Authorized ✅

Group Chat ID: {chat_id}

Message: This Group (<code>{chat_id}</code>) is Successfully Authorized .
       </b> """
                await message.reply_text(resp, message.id)
                
                chat_resp = f"""<b>
Authorized ✅

Group Chat ID: {chat_id}

Message: This Group is now Authorized For using Our Bot . Authorized By @stripe_xD
       </b> """
                try:
                    await Client.send_message(chat_id, chat_resp)
                except:
                    pass

            else:
                find = await getchatinfo(chat_id)
                find = str(find)
                if find != "None":
                    resp = f"""<b>
Already Authorized ⚠️

Group Chat ID: {chat_id}

Message: This Group (<code>{chat_id}</code>) is Already Authorized .
       </b> """
                    await message.reply_text(resp, message.id)

    except Exception as e:
        await message.reply_text(e, message.id)
        import traceback
        await error_log(traceback.format_exc())

import traceback , json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

async def chops_set(user_id):
    try:
        import pymongo
        from mongodb import client, usersdb
        prev = {"id": f"{user_id}"}
        nextt = {"$set": {f"status": "Admin"}}
        update = usersdb.update_one(prev, nextt)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

@Client.on_message(filters.command("addadmin", [".", "/"]))
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
                user_id = str(message.text.split(" ")[1])
            except:
                return
            await chops_set(user_id)
            resp = f"""<b>
Role Added Successfully ✅ 
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Role :  Admin

Status : Successfull
    </b> """
            await message.reply_text(resp, message.id)

            user_resp = f"""<b>
Role Added Successfully ✅ 
━━━━━━━━━━━━━━ 
User ID: {user_id} 
Role: Admin 

Message: Congratz ! Your Account Successfully Promoted To "Admin" User . Enjoy Yourself on the Bot .
    </b> """
            await Client.send_message(user_id, user_resp)



    except Exception as e:
        await message.reply_text(e, message.id)
        import traceback
        await error_log(traceback.format_exc())

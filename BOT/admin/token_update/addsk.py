import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *

@Client.on_message(filters.command("addsk", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        
        if user_id != OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️
            
Message: To perform this action, you need admin level power. 
            
Contact @stripe_xD For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        # Check if there is a reply to a message
        if message.reply_to_message and message.reply_to_message.text:
            sk_and_pk = message.reply_to_message.text.split('\n')
            
            # Check if there are both SK and PK
            if len(sk_and_pk) == 2:
                sk, pk = sk_and_pk
                await addsk(sk, pk)
                
                resp = f"""<b>
SK Key (Stripe Key) and PK Key (Public Key) Successfully Added ✅
━━━━━━━━━━━━━━
SK: {sk}
PK: {pk}

Status: Successful
</b>"""
                await message.reply_text(resp, message.id)
            else:
                await message.reply_text("<b>Please provide both SK and PK in separate lines.</b>", message.id)
        else:
            await message.reply_text("<b>Reply to a message containing both SK and PK to add them.</b>", message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())

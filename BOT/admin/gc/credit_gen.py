import json
from .func import *
from pyrogram import Client, filters


@Client.on_message(filters.command("gc", [".", "/"]))
async def cmd_gc(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id != OWNER_ID:
            resp = """<b>
Privilege Not Found ⚠️

Message: Do Perfom This Action , You Need Admin Level Power . 

Contact @stripe_xD For More Info ✅` 

</b>"""
            await message.reply_text(resp, message.id)
        else:
            try:
                amt = int(message.text.split(" ")[1])
            except:
                amt = 10
   
            text = f"""<b>Giftcode Genarated ✅
Amount: {amt}\n</b>"""
            
            for _ in range(amt):
                GC = f"Mahico-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
                await insert_pm(GC)
                text += f"""
➔ <code>{GC}</code>
<b>Value : 100 Credits + Premium</b>\n"""

            text += f"""
<b>For Redeemtion 
Type /redeem Mahico-XXXX-XXXX-XXXX</b>"""
            await message.reply_text(text, message.id)
            
    except:
        import traceback
        await error_log(traceback.format_exc())
        

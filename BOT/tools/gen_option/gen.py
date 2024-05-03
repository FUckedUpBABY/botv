import httpx
from pyrogram import Client, filters
import os
import threading
import asyncio
import time
from FUNC.usersdb_func import *
from FUNC.cc_gen import *
from TOOLS.check_all_func import *


@Client.on_message(filters.command("gen", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(gen_cmd(Client, message))
    loop.close()


async def gen_cmd(Client, message):
    try:
        user_id, chat_type, chat_id = (
            str(message.from_user.id),
            str(message.chat.type),
            str(message.chat.id),
        )
        checkall = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            ccsdata = message.text.split(" ")[1]
            cc = ccsdata.split("|")[0]
        except:
            resp = f"""
Wrong Format ❌

Usage:
Only Bin
<code>/gen 447697</code>

With Expiration
<code>/gen 447697|12</code>
<code>/gen 447697|12|23</code>

With CVV
<code>/gen 447697|12|23|000</code>

With Custom Amount
<code>/gen 447697 100</code>
"""
            await message.reply_text(resp, message.id)
            return
        try:
            mes = ccsdata.split("|")[1]
        except:
            mes = None

        try:
            ano = ccsdata.split("|")[2]
        except:
            ano = None

        try:
            cvv = ccsdata.split("|")[3]
        except:
            cvv = None

        try:
            amount = int(message.text.split(" ")[2])
        except:
            amount = 15

        delete = await message.reply_text("<b>Genarating...</b>", message.id)
        await asyncio.sleep(0.5)
        start = time.perf_counter()
        session = httpx.AsyncClient(timeout=30)
        getbin = await get_bin_details(cc[:6], session)
        await session.aclose()
        brand, type, level, bank, country, flag, currency = (
            getbin[0],
            getbin[1],
            getbin[2],
            getbin[3],
            getbin[4],
            getbin[5],
            getbin[6],
        )

        if amount > 10000:
            resp = """<b>Limit Reached ⚠️

Message: Maximum Genarated Amount is 10K .</b>"""
            await message.reply_text(resp, message.id)
            return

        if amount == 15:
            all_cards = await luhn_card_genarator(cc, mes, ano, cvv, 15)
            resp = f"""<b>
Credit Card Genarated Successfully ✅
━━━━━━━━━━━━━━ 
BIN : {cc}
Genarated Amount : {amount}
Algorithm : Luhn 

BIN Info :
Bin - {cc[:6]} - {brand} - {type} - {level}
Bank - {bank} 
Country - {country} - {flag} - {currency}

<code>{all_cards}</code>

Genned By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
Time Taken: {int(time.perf_counter() - start)}𝘀
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b> """
            await Client.delete_messages(message.chat.id, delete.id)
            await message.reply_text(resp, message.id)

        else:
            filename = f"downloads/{amount}x_CC_Genarated_By_{user_id}.txt"
            all_cards = await luhn_card_genarator(cc, mes, ano, cvv, amount)
            with open(filename, "a") as f:
                f.write(f"{all_cards}\n")

            caption = f"""<b>
Credit Card Genarated Successfully ✅
━━━━━━━━━━━━━━ 
BIN : {cc}
Genarated Amount : {amount}
Algorithm : Luhn 

BIN Info :
Bin - {cc[:6]} - {brand} - {type} - {level}
Bank - {bank} 
Country - {country} - {flag} - {currency}

Genned By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
Time Taken: {int(time.perf_counter() - start)}𝘀
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a></b>"""
            await Client.delete_messages(message.chat.id, delete.id)
            await message.reply_document(
                document=filename,
                caption=caption,
                reply_to_message_id=message.id,
            )
            os.remove(filename)

    except:
        import traceback
        await error_log(traceback.format_exc())

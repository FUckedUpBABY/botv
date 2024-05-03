import json
import time
import threading
import asyncio
import httpx
from pyrogram import Client, filters
from datetime import timedelta
from FUNC.usersdb_func import *
from FUNC.defs import *
from .gate import *
from .response import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_mass import *



async def mchkfunc(fullcc , user_id ):
    try:  
        proxies  = await get_proxy_format()
        session  = httpx.AsyncClient(timeout = 30 , proxies = proxies ) 
        result   = await create_cvv_charge(fullcc , session) 
        getresp  = await get_charge_resp(result, user_id, fullcc)
        response = getresp["response"]
        
        await session.aclose()
        return f"<code>{fullcc}</code>\n<b>Result - {response}</b>\n"

    except:
        import traceback
        await error_log(traceback.format_exc())
        return f"<code>{fullcc}</code>\n<b>Result - Card Declined 🚫</b>\n"
    

@Client.on_message(filters.command("mchk1", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_auth_cmd(Client, message))
    loop.close()


async def stripe_mass_auth_cmd(Client, message):
    try:
        user_id    = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall   = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role  = checkall[1]
        getcc = await getcc_for_mass(message, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs  = getcc[1]
        resp = f"""<b>
Gate : Mass Stripe CVV Charge 1$ 💋️

CC Amount : {len(ccs)}
Message : Checking CC For {first_name}

Status : Processing...⌛️

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
        </b> """
        nov = await message.reply_text(resp, message.id)

        text = f"""
<b>↯ MASS STRIPE CHARGE</b> \n
"""
        amt        = 0
        start      = time.perf_counter()
        # proxies    = await get_proxy_format()
        # session    = httpx.AsyncClient(timeout = 100 , proxies = proxies , follow_redirects = True )  
        works      = [mchkfunc(i, user_id ) for i in ccs]
        worker_num = int(json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["THREADS"])

        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                amt += 1
                text += i
                if amt % 5 == 0:
                    try:
                        await Client.edit_message_text(message.chat.id, nov.id, text)
                    except:
                        pass
            await asyncio.sleep(1)
            works = works[worker_num:]
        

        # await session.aclose()
        taken                     = str(timedelta(seconds=time.perf_counter() - start))
        hours , Min , seconds = map(float, taken.split(":"))
        hour                      = int(hours)
        min                       = int(Min)
        sec                       = int(seconds)

        text += f"""



Total CC Checked - {len(ccs)}
Credit Deducted - {len(ccs)}
Time Taken - {hour} Hours {min} Min {sec} Seconds
Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role}]
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
Owner - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>

"""
        await Client.edit_message_text(message.chat.id, nov.id, text)
        await massdeductcredit(user_id, len(ccs))
        await setantispamtime(user_id)

    except:
        import traceback
        await error_log(traceback.format_exc())

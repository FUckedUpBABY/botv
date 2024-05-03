import time
import httpx
import threading
import asyncio
import json
from pyrogram import Client, filters
from datetime import timedelta
from .gate import *
from .response import *
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_txt import *


async def get_checked_done_response(Client , message , ccs ,  key , hitsfile , start , stats , role , chk_done , charged , live):
    try:
        taken                     = str(timedelta(seconds=time.perf_counter() - start))
        hours , Min , seconds = map(float, taken.split(":"))
        hour                      = int(hours)
        min                       = int(Min)
        sec                       = int(seconds)
        if live != 0 or charged != 0:
            await Client.delete_messages(message.chat.id, stats.id)
            text = f"""<b>
Gates: Mass Stripe CVV Charge 0.5$ SK Based 💋️

Total CC Input: {len(ccs)}
Charged: {charged} 
Live: {live}
Dead: { chk_done - charged - live }
Total Checked: {chk_done}
Secret Key: <code>{key}</code>
Status: Checked All ✅

Checked By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role}]
Credit Will Be Deducted - {len(ccs)} 
Time Taken - {hour} Hours {min} Min {sec} Seconds
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
</b>"""
            await message.reply_document(document = hitsfile , caption = text , reply_to_message_id = message.id)

        else:
            text = f"""<b>
Gates: Mass Stripe CVV Charge 0.5$ SK Based 💋️

Total CC Input: {len(ccs)}
Charged: {charged} 
Live: {live}
Dead: { chk_done - charged - live }
Total Checked: {chk_done}
Secret Key: <code>{key}</code>
<i>( Get Your Hits Key By "/gethits {key}" )</i>
Status: Checked All ✅

Checked By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role}]
Credit Will Be Deducted - {len(ccs)} 
Time Taken - {hour} Hours {min} Min {sec} Seconds
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
</b>"""
            await Client.edit_message_text(message.chat.id, stats.id, text )
    except:
        pass


async def get_checking_response(Client , message , ccs ,  key , i , start , stats , role , charged , live , chk_done):
    try:
        taken                     = str(timedelta(seconds=time.perf_counter() - start))
        hours , Min , seconds = map(float, taken.split(":"))
        hour                      = int(hours)
        min                       = int(Min)
        sec                       = int(seconds)
        cc                        = i["fullz"]
        response                  = i["response"]
        text = f"""<b>
Gates: Mass Stripe CVV Charge 0.5$ SK Based 💋️

<code>{cc}</code>
Result - {response}

Total CC Input: {len(ccs)}
Charged: {charged} 
Live: {live}
Dead: { chk_done - charged - live }
Total Checked: {chk_done}
Secret Key: <code>{key}</code>
<i>( Get Your Hits Key By "/gethits {key}" )</i>
Status: Checking...


Checked By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role}]
Credit Will Be Deducted - {len(ccs)} 
Time Taken - {hour} Hours {min} Min {sec} Seconds
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
</b>"""
        await Client.edit_message_text(chat_id = message.chat.id , message_id = stats.id , text = text)
    except:
        pass


async def mchktxtfunc(fullcc , sks ,pk, user_id , session):
    getresp   = await skcvv_basedCode(sks,pk,fullcc,session)
    return getresp
 
    
async def gcgenfunc(len=4):
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(len))

    
async def save_cc(i, file_name):
    try:       
        cc       = i["fullz"]
        response = i["response"]
        hitsfile = f"HITS/{file_name}"
        with open(hitsfile, "a", encoding="utf-8") as f:
            f.write(f"{cc}\nResult - {response}\n")
    except:
        pass


@Client.on_message(filters.command("cvvtxt", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_txt_auth_cmd(Client, message))
    loop.close()


async def stripe_mass_txt_auth_cmd(Client, message):
    try:
        user_id    = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall   = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            random_text = await gcgenfunc(len=8)
            key         = f"mchktxt_{message.from_user.id}_{random_text}"
            file_name   = f"{key}.txt"
            hitsfile    = f"HITS/{file_name}"
            await message.reply_to_message.download(file_name = file_name)
        except:
            resp = """<b>
Gate Name: Mass Stripe CVV Charge 0.5$ SK Based 💋️
CMD: /cvvtxt

Message: No CC Found in your input ❌

Usage: /cvvtxt [ in reply to txt file ]
        </b> """
            await message.reply_text(resp, message.id)
            return

        getcc = await getcc_for_txt(file_name, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs  = getcc[1]
        text = f"""<b>
Gate : Mass Stripe CVV Charge 0.5$ SK Based 💋️

CC Amount : {len(ccs)}
Message : Checking CC For {first_name}
Note: This Pop Up Will Change After 50 CC Checked . So Keep Patient . 

Status : Processing...⌛️

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
    </b> """
        stats = await message.reply_text(text, message.id)
        hits_count   = 0
        chk_done     = 0
        charged      = 0
        live         = 0
        start        = time.perf_counter()
        sks      = "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"
        pk       = "pk_live_CEHlBZCWH3uFCiJbd3tiPgum"
        session      = httpx.AsyncClient(timeout = 30 )
        works = [mchktxtfunc(i, sks, pk, user_id, session) for i in ccs]
        worker_num   = int(json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["THREADS"])

        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                chk_done += 1
                if i["hits"] == "yes":
                    hits_count += 1
                    await save_cc(i, file_name)

                if chk_done % 50 == 0:
                   await get_checking_response(Client , message , ccs ,  key , i , start , stats , role , hits_count , chk_done)

            works = works[worker_num:]

        await session.aclose()
        await get_checked_done_response(Client , message , ccs ,  key , hitsfile , start , stats , role , charged , live , chk_done)
        await massdeductcredit(user_id, len(ccs))
        await setantispamtime(user_id)

    except:
        import traceback
        await error_log(traceback.format_exc())

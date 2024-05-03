import asyncio
import httpx
from datetime import timedelta
from pyrogram import Client, filters
from .gate import *
from .response import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_mass import *

async def mchkfunc(fullcc, sks, pk, user_id, session):
    try:
        getresp = await skcvv_basedCode(sks, pk, fullcc, session)
        status   = getresp["status"]
        response = getresp["response"]
        return f"<code>{fullcc}</code>\n<b>Result - {response}</b>\n"
    except Exception as e:
        await error_log(str(e))
        return f"<code>{fullcc}</code>\n<b>Result - Card Declined 🚫</b>\n"

@Client.on_message(filters.command("masscvv", [".", "/"]))
async def multi(Client, message):
    user_id = str(message.from_user.id)
    checkall = await check_all_thing(Client, message)
    if not checkall[0]:
        return

    role = checkall[1]
    getcc = await getcc_for_mass(message, role)
    if not getcc[0]:
        await message.reply_text(getcc[1], message.id)
        return

    ccs = getcc[1]
    resp = f"""<b>
Gate : Mass Stripe CVV Charge 0.5$ SK Based 💋️

CC Amount : {len(ccs)}
Message : Checking CC For {message.from_user.first_name}

Status : Processing...⌛️

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
        </b> """
    nov = await message.reply_text(resp, message.id)

    text = f"""
<b>↯ MASS STRIPE CHARGE</b> \n
"""
    amt, start = 0, time.perf_counter()
    proxies = await get_proxy_format()
    session = httpx.AsyncClient(timeout=30, proxies=proxies, follow_redirects=True)
    sks      = "sk_live_AwMlaqltuwCMwwl7mxaGsQfN"
    pk       = "pk_live_93urvOTbs6SjUQm0K3GXBnnV"
    
    works = [mchkfunc(i, sks, pk, user_id, session) for i in ccs]
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

    await session.aclose()
    taken_seconds = int(time.perf_counter() - start)
    hours = taken_seconds // 3600
    Min = (taken_seconds % 3600) // 60
    seconds = taken_seconds % 60

    
    text += f"""



Total CC Checked - {len(ccs)}
Credit Deducted - {len(ccs)}
Time Taken - {hours} Hours {Min} Min {seconds} Seconds
Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role}]
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
Owner - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>

"""
    await Client.edit_message_text(message.chat.id, nov.id, text)
    await massdeductcredit(user_id, len(ccs))
    await setantispamtime(user_id)

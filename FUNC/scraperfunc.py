import time , os
from FUNC.defs import *
from datetime import timedelta


async def cc_public_scrape(message, user, bot, channel_link, limit, delete, role):
    try:
        start = time.perf_counter()
        ccs, amt, dublicate = [] , 0 , 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = await getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            ccs.append(getcc)
                            amt += 1

            except:
                getcc = await getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)
        else:
            file_name = f"downloads/{amt}x_CC_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="utf-8") as f:
                for x in ccs:
                    cc, mes, ano, cvv = x[0], x[1], x[2], x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")

            chat_info = await user.get_chat(channel_link)
            title = chat_info.title 
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
CC Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)


async def check_invite_link(user, channel_link):
    try:
        chat_info = await user.get_chat(channel_link)
        channel_id, title = chat_info.id, chat_info.title
        return True, channel_id, title
    except:
        try:
            join = await user.join_chat(channel_link)
            title, channel_id = join.title, join.id
            return True, channel_id, title
        except:
            import traceback
            await error_log(traceback.format_exc())
            return False


async def cc_private_scrape(message, user, bot, channel_id, channel_title, limit, role):
    try:
        start = time.perf_counter()
        ccs, amt, dublicate = [], 0, 0
        resp = f"""<b>
Gate: CC Scraper 💋️

Message: Scraping {limit} CC From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = await getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            ccs.append(getcc)
                            amt += 1

            except:
                getcc = await getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"downloads/{amt}x_CC_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="UTF-8") as f:
                for x in ccs:
                    cc, mes, ano, cvv = x[0], x[1], x[2], x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
CC Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)


async def bin_public_scrape(
    message, user, bot, scrape_bin, channel_link, limit, delete, role
):
    try:
        start = time.perf_counter()
        ccs = []
        amt = 0
        dublicate = 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = await getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            if scrape_bin in getcc[0][:6]:
                                ccs.append(getcc)
                                amt += 1

            except:
                getcc = await getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"downloads/{amt}x_CC_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="UTF-8") as f:
                for x in ccs:
                    cc, mes, ano, cvv = x[0], x[1], x[2], x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            chat_info = await user.get_chat(channel_link)
            title = chat_info.title 
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
CC Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● Targeted Bin: {scrape_bin}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)


async def bin_private_scrape(
    message, user, bot, scrape_bin, channel_id, channel_title, limit, role
):
    try:
        start = time.perf_counter()
        ccs, amt, dublicate = [], 0, 0
        resp = f"""<b>
Gate: CC Scraper 💋️

Message: Scraping {limit} CC From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = await getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            if scrape_bin in getcc[0][:6]:
                                ccs.append(getcc)
                                amt += 1

            except:
                getcc = await getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"downloads/{amt}x_CC_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="UTF-8") as f:
                for x in ccs:
                    cc, mes, ano, cvv = x[0], x[1], x[2], x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
CC Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● Targeted Bin: {scrape_bin}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())

        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)


async def sk_public_scrape(message, user, bot, channel_link, limit, delete, role):
    try:
        start = time.perf_counter()
        ccs, amt, dublicate = [], 0, 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            if "sk_live" in msg:
                sk = msg.split("sk_live")[1].split(" ")[0]
                if "xxxxx" in sk:
                    pass
                else:
                    if "\n" in sk:
                        sk = sk.split("\n")[0]
                    if "✅" in sk:
                        sk = sk.splice("✅")[1]
                    sk = "sk_live" + sk
                    if sk in ccs:
                        dublicate += 1
                    else:
                        amt += 1
                        ccs.append(sk)

        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No SK Found ❌

Message: We Didnt Find Any SK In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"downloads/{amt}x_SK_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="UTF-8") as f:
                for x in ccs:
                    f.write(f"{x}\n")
            chat_info = await user.get_chat(channel_link)
            title = chat_info.title
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
SK Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● SK Found: {amt}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)


async def sk_private_scrape(message, user, bot, channel_id, channel_title, limit, role):
    try:
        start = time.perf_counter()
        ccs, amt, dublicate = [], 0, 0
        resp = f"""<b>
Gate: SK Scraper 💋️

Message: Scraping {limit} SK From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            if "sk_live" in msg:
                sk = msg.split("sk_live")[1].split(" ")[0]
                if "xxxxx" in sk:
                    pass
                else:
                    if "\n" in sk:
                        sk = sk.split("\n")[0]
                    if "✅" in sk:
                        sk = sk.splice("✅")[1]
                    sk = "sk_live" + sk
                    if sk in ccs:
                        dublicate += 1
                    else:
                        amt += 1
                        ccs.append(sk)

        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No SK Found ❌

Message: We Didnt Find Any SK In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"downloads/{amt}x_SK_Scraped_For_{message.from_user.id}_By_@chkmtc_bot.txt"
            with open(file_name, "a", encoding="UTF-8") as f:
                for x in ccs:
                    f.write(f"{x}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            taken = str(timedelta(seconds=time.perf_counter() - start))
            hour, min, sec = taken.split(":")
            hour, min, sec = int(hour), int(min), int(float(sec))
            caption = f"""<b>
SK Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 💋️ [ {role} ]
● Time Taken: {min} Min {sec} Seconds
● Bot by - <a href="tg://user?id=5371579102">⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</b>
"""
            await message.reply_document(
                document=file_name, caption=caption, reply_to_message_id=message.id
            )

            os.remove(file_name)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{str(e)}</b>", message.id)

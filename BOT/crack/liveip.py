import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pyrogram import Client, filters
from pyrogram.types import Message
import time
import requests
from FUNC.defs import *
from TOOLS.check_all_func import *

# List of common subdomains
received_files = {}  # Dictionary to store received files
start_time = 0  # Initialize start_time

# Define the chat ID of the separate chat where you want to send live IPs
separate_chat_id = "-1002140459626"

# The 'valid' function for checking IP liveness
def check_ip(ip):
    try:
        response = requests.get(f'http://{ip}', timeout=0.3)
        if response.status_code == 200:
            print(f"Live IP: {ip}")
            return ip
        else:
            print(f"Dead IP: {ip}")
    except Exception as e:
        print(f"DEAD IP {ip}")

@Client.on_message(filters.command('live'))
async def check_live_ips(client, message: Message):
    try:
         
        # user_id, chat_type, chat_id = (
        #     str(message.from_user.id),
        #     str(message.chat.type),
        #     str(message.chat.id),
        # )
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]
        getcc = await getmessage(message)
        if getcc is False:
            start_time = time.time()  # Record the start time

            command = message.text.split()
           
        if message.reply_to_message and message.reply_to_message.document:
            document = message.reply_to_message.document
            file_id = document.file_id

            # Download the file to the current working directory
            file_path = await client.download_media(file_id)

            with open(file_path, 'r') as file:
                ip_list = file.read().splitlines()

            start_time = time.time()
            print("Starting IP checking...")

            with ThreadPoolExecutor() as executor:
                loop = asyncio.get_event_loop()
                live_ips = await loop.run_in_executor(executor, lambda: [check_ip(ip) for ip in ip_list])

            end_time = time.time()
            time_taken = end_time - start_time
            print(f"IP checking completed in {time_taken:.2f} seconds")

            live_ips = [ip for ip in live_ips if ip is not None]  # Filter out None values

            if live_ips:
                file_name = "live_ips.txt"
                with open(file_name, "w") as file:
                    file.write('\n'.join(live_ips))

                text = f"""<b>
🌐 Live IP Check Completed 🌐
Live IPs found: {len(live_ips)}
CHECKED BY <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>{role}
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
OWNER - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>
TIME TAKEN: <code>{time_taken:.2f}</code> seconds
</b>"""

                await message.reply_document(
                    document=file_name,
                    caption=text,
                )

                try:
                    separate_chat = await client.get_chat(chat_id=separate_chat_id)
                    await separate_chat.send_document(
                        document=file_name,
                        caption=f"Live IPs found during scanning. ({len(live_ips)} live IPs)"
                    )
                except Exception as e:
                    with open("error_logs.txt", "a") as f:
                        f.write(f"Error sending the document to the separate chat: {e}\n")

                os.remove(file_name)
            else:
                await message.reply(f"""<b>
🌐 Live IP Check Completed 🌐
No Live IPs Found
CHECKED BY <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
OWNER - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>
TIME TAKEN: <code>{time_taken:.2f}</code> seconds
</b>""")
        else:
            await message.reply("Please reply to a document containing IPs with /live.")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

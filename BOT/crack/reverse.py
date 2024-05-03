import os
from pyrogram import Client, filters
from pyrogram.types import Message
import socket
import asyncio
import time
from FUNC.defs import *
from TOOLS.check_all_func import *

received_files = {}  # Dictionary to store received files

async def reverse_domain_async(domains):
    ips = []
    for domain in domains:
        try:
            ip = await asyncio.to_thread(socket.gethostbyname, domain)
            ips.append(f"{domain} -> {ip}")
        except Exception as e:
            ips.append(f"{domain} -> Error: {str(e)}")
    return ips

@Client.on_message(filters.command('reverse'))
async def reverse_domain(client, message: Message):
    try:
         
        user_id, chat_type, chat_id = (
            str(message.from_user.id),
            str(message.chat.type),
            str(message.chat.id),
        )
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
            quantity = int(command[1])
        start_time = time.time()  # Record the start time

        # Initialize time_taken to a default value
        time_taken = 0.0

        # Check if the message is a reply and contains a document
        if message.reply_to_message and message.reply_to_message.document:
            document = message.reply_to_message.document
            file_id = document.file_id

            # Download the file
            file_path = await client.download_media(file_id)

            # Read the domains from the file
            with open(file_path, 'r') as file:
                domains = file.read().splitlines()

            # Perform domain-to-IP conversion asynchronously
            ips = await reverse_domain_async(domains)

            # Count the number of successfully reversed domains
            success_count = sum(1 for result in ips if 'Error' not in result)

            if success_count > 0:
                # Create a text file with the converted IPs
                file_name = "converted_ips.txt"
                with open(file_name, "w") as file:
                    file.write("\n".join(ips))

                end_time = time.time()  # Record the end time
                time_taken = end_time - start_time  # Calculate time taken in seconds

            message_text = f"""<b>
Domain to IP Conversion Completed
Successful Conversions: {success_count}
CHECKED BY <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>{role}
Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
OWNER - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>
TIME TAKEN: <code>{time_taken:.2f}</code> seconds
</b>"""

            if success_count > 0:
                # Send the text file as a document
                await message.reply_document(
                    document=file_name,
                    caption="Domain to IP conversion results",
                    text=message_text
                )
                os.remove(file_name)  # Remove the temporary file
            else:
                # Send a text message
                await message.reply(message_text)

        else:
            await message.reply("Please reply to a document containing a list of domains with /reverse.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

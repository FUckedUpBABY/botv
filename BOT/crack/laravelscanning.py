import os
import asyncio
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from bs4 import BeautifulSoup
import time
from FUNC.defs import *
from TOOLS.check_all_func import *
# # List of common subdomains
# app = Client("my_bot")

# Initialize aiohttp.ClientSession
# session = aiohttp.ClientSession()

received_files = {}  # Dictionary to store received files
start_time = 0  # Initialize start_time

# Define the chat ID of the separate chat where you want to send Laravel sites
separate_chat_id = "-1002140459626"

# ...

async def scan_for_laravel_sites(session, urls):
    laravel_sites = []

    async def check_url(url):
        try:
            async with session.get(url, timeout=30) as response:
                if response.status == 200:
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    text = soup.text.lower()

                    # Check for keywords, endpoints, and subdomains
                    # Add more checks as needed

                    # Check for Laravel cookies
                    if "laravel_session" in response.cookies and "laravel_token" in response.cookies:
                        laravel_sites.append(url)
                        # Send the Laravel site to the separate chat
                        await client.send_message(separate_chat_id, f"Laravel Site Found: {url}")

                    await asyncio.sleep(1)

        except aiohttp.ClientError as e:
            print(f"AIOHTTP error while scanning URL '{url}': {e}")
        except Exception as e:
            print(f"Error while scanning URL '{url}': {e}")

    tasks = [check_url(url) for url in urls]
    await asyncio.gather(*tasks)

    return laravel_sites

# ...

@Client.on_message(filters.command('scanlaravel'))
async def scan_laravel(client, message: Message):
    global start_time, laravel_sites  # Declare laravel_sites at the global level
    laravel_sites = []  # Initialize laravel_sites as an empty list
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
        # Check if the message is a reply and contains a document
        if message.reply_to_message and message.reply_to_message.document:
            document = message.reply_to_message.document
            file_id = document.file_id

            # Download the file
            file_path = await client.download_media(file_id)

            # Read the URLs from the file
            with open(file_path, 'r') as file:
                received_urls = file.read().splitlines()

            start_time = time.time()  # Record the start time

            # Pass both session and received_urls to the function
            await scan_for_laravel_sites(received_urls)

            # ...

            # Record the end time
            end_time = time.time()
            time_taken = end_time - start_time  # Calculate time taken in seconds

            if laravel_sites:
                file_name = "laravel_sites.txt"
                with open(file_name, "w") as file:
                    for site in laravel_sites:
                        file.write(site + "\n")

                # Create the message text
                message_text = f"""<b>
🍀 Laravel Scanning Completed 🍀
<a>Quantity-{len(laravel_sites)}</a>
CHECKED BY <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>{role}
BOT BY  - <a href="https://t.me/blackhatarmy_xd">BLACKHATARMY</a>
TIME TAKEN: <code>{time_taken:.2f}</code> seconds
</b>"""

                # Send the document to the user
                await message.reply_document(
                    document=file_name,
                    caption="Laravel Sites found during scanning:",
                    text=message_text  # Set the caption text
                )

                # Send the document to the separate chat
                await Client.send_document(separate_chat_id, file_name, caption="Laravel Sites found during scanning:")

                os.remove(file_name)
            else:
                await message.reply(f"""<b>
🍀 Laravel Scanning Completed 🍀
<a>FOUND-{len(laravel_sites)}</a>
CHECKED BY <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>{role}
BOT BY  - <a href="https://t.me/blackhatarmy_xd">BLACKHATARMY</a>
TIME TAKEN: <code>{time_taken:.2f}</code> seconds
</b>""")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

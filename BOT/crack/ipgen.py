import os
import random
import ipaddress
import time
from pyrogram import Client, filters
from pyrogram.types import Message
import json
from FUNC.defs import *
from TOOLS.check_all_func import *

user_last_command_time = {}
ROLES = {
    "free": {"ip_limit": 200000, "cooldown": 10},
    "premium": {"ip_limit": 500000, "cooldown": 3},
    "admin": {"ip_limit": 1000000, "cooldown": 2},
    "ceo": {"ip_limit": 2000000, "cooldown": 1},
}

def generate_valid_ip(ip_type):
    while True:
        if ip_type == "ipv4":
            ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        else:
            ip = ":".join(format(random.randint(0, 65535), 'x') for _ in range(8))
        try:
            ipaddress.ip_address(ip)  # Check if the generated IP address is valid
            return ip
        except ValueError:
            continue  # If not valid, try again

@Client.on_message(filters.command('genip'))
async def generate_ip_address(client, message: Message):
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
            ip_type = command[-1].lower()

            if ip_type not in ["ipv4", "ipv6"]:
                await message.reply("Invalid IP type. Please use 'ipv4' or 'ipv6'.")
                return

            ip_list = [generate_valid_ip(ip_type) for _ in range(quantity)]

            file_name = f'generated_ips_{quantity}_{ip_type}.txt'
            with open(file_name, 'w') as file:
                for ip in ip_list:
                    file.write(ip + '\n')

            end_time = time.time()  # Record the end time
            time_taken = end_time - start_time  # Calculate time taken in seconds

            text = f"""<b>
          🍀Ip Generated Successfully🍀
    Quantity <code>{quantity}</code>
    Type<code>{ip_type}</code>
    Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> <code>{role} </code>
    Updates  - <a href="https://t.me/NoMoreBins">三 𝙉𝙤 𝙈𝙤𝙧𝙚 𝘽𝙞𝙣𝙨 三</a>
    OWNER - <a href="https://t.me/stripe_xD">>⏤͟͞🇧🇩⌁𝙒𝙞𝙣𝙩𝙚𝙧𝙜𝙧𝙚𝙚𝙣 𝙈𝙖𝙧𝙨ヤ</a>
    Time Taken: <code>{time_taken:.2f} </code>seconds
            </b>"""

            await message.reply_document(
                document=file_name, caption=text
            )

            os.remove(file_name)

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

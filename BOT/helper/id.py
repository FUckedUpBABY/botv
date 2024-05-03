from pyrogram import Client, filters
from FUNC.usersdb_func import *


async def get_user_info(user_id, Client, message):
    try:
        user_id = str(message.text.split(" ")[1])
        get = await Client.get_users(user_id)
        name, id, username, restriction, scam, premium = (
            get.first_name,
            get.id,
            get.username,
            get.is_restricted,
            get.is_scam,
            get.is_premium,
        )
        resp = f"""<b>
Info of '{user_id}' on Telegram
━━━━━━━━━━━━━━
● Firstname: {name}
● ID: {id}
● Username: {username}
● Profile Link: <a href="tg://user?id={id}">Profile Link</a>
● TG Restrictions: {restriction}
● TG Scamtag: {scam}
● TG Premium: {premium}
    </b> """
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())


@Client.on_message(filters.command("id", [".", "/"]))
async def cmd_id(Client, message):
    try:
        try:
            if message.text.split(" ")[1]:
                await get_user_info(message.text.split(" ")[1], Client, message)
                return

        except:
            if message.reply_to_message:
                texta = f"""<b>
Hey <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !
Your User ID: <code>{message.reply_to_message.from_user.id}</code> 
This Chat ID: <code>{message.chat.id}</code>
    </b>"""
                await message.reply_text(texta, message.id)

            else:
                texta = f"""<b>
Hey <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !
Your User ID: <code>{message.from_user.id}</code> 
This Chat ID: <code>{message.chat.id}</code>
    </b>"""
                await message.reply_text(texta, message.id)
    except:
        import traceback
        await error_log(traceback.format_exc())

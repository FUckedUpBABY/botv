from pyrogram import Client, filters


@Client.on_message(filters.command("getuser", [".", "/"]))
async def cmd_cmds(Client, message):
    try:
        user = message.text.split(" ")[1]
    except:
        resp = f"""<b>
Usage:
/getuser id_or_username
    </b>"""
        await message.reply_text(resp, message.id)
        return

    try:
        get = await Client.get_users(user)
        name , id , username , restriction , scam , premium = get.first_name , get.id , get.username , get.is_restricted , get.is_scam , get.is_premium
        resp = f"""<b>
Info of '{user}' on Telegram
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

    except Exception as e:
        await message.reply_text("<b>Invalid Username or Incorrect ID ❌</b>", message.id)


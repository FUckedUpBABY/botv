from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("info", [".", "/"]))
async def cmd_info(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = await getuserinfo(user_id)
        results = str(regdata)
        if results == "None":
            resp = """<b>
Unregistered Users ⚠️

Message: You Can't Use Me Unless You Register First .

Type /register to Continue
</b>"""
            await message.reply_text(resp, message.id)
            return

        if message.reply_to_message:
            user_id, username, first_name = (
                str(message.reply_to_message.from_user.id),
                str(message.reply_to_message.from_user.username),
                str(message.reply_to_message.from_user.first_name),
            )
            results = await getuserinfo(user_id)
            status, plan, expiry, credit, antispam_time, totalkey, reg_at = (
                results["status"],
                results["plan"],
                results["expiry"],
                results["credit"],
                results["antispam_time"],
                results["totalkey"],
                results["reg_at"],
            )
            send_info = f"""<b>
Your Info on Mahico Checker ⚡
━━━━━━━━━━━━━━
● Firstname: {first_name}
● ID: <code>{user_id}</code>
● Username: {username}
● Profile Link: <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
● TG Restrictions: {message.reply_to_message.from_user.is_restricted}
● TG Scamtag: {message.reply_to_message.from_user.is_scam}
● TG Premium: {message.reply_to_message.from_user.is_premium}
● Status: {status}
● Credit: {credit}
● Plan: {plan}
● Plan Expiry: {expiry}
● Key Redeemed : {totalkey}
● Registered at: {reg_at}</b>
"""
            await message.reply_text(send_info, message.id)
        else:
            user_id, username, first_name = (
                str(message.from_user.id),
                str(message.from_user.username),
                str(message.from_user.first_name),
            )
            results = await getuserinfo(user_id)
            status, plan, expiry, credit, antispam_time, totalkey, reg_at = (
                results["status"],
                results["plan"],
                results["expiry"],
                results["credit"],
                results["antispam_time"],
                results["totalkey"],
                results["reg_at"],
            )
            send_info = f"""<b>
Your Info on Mahico Checker ⚡⚡
━━━━━━━━━━━━━━
● Firstname: {first_name}
● ID: <code>{user_id}</code>
● Username: {username}
● Profile Link: <a href="tg://user?id={message.from_user.id}">Profile Link</a>
● TG Restrictions: {message.from_user.is_restricted}
● TG Scamtag: {message.from_user.is_scam}
● TG Premium: {message.from_user.is_premium}
● Status: {status}
● Credit: {credit}
● Plan: {plan}
● Plan Expiry: {expiry}
● Key Redeemed : {totalkey}
● Registered at: {reg_at}</b>
"""
        await message.reply_text(send_info, message.id)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())

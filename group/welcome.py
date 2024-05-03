from pyrogram import Client, filters
import random


gif = [
    "https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4",
]


MESSAGE = """<b>
Hey My Boy {} !
Welcome To Our Group ❤️

Please Follow Some Rules :
1. Don't Send Unwanted Links To Here.
2. Don't Spam.
3. Promo Of Your Channel is Prohibited.

Also Just Press /register Once For Continously Using Me🥰
</b>"""


@Client.on_message(filters.new_chat_members)
async def welcome(Client, message):
    try:
        new_members = [u.mention for u in message.new_chat_members]
        text = MESSAGE.format(",".join(new_members))
        img = random.choice(gif)
        await message.reply_video(
                    video= img,
                    caption= text , 
                    quote=True,
                )
    except:
        pass

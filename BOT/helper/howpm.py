from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("howpm", [".", "/"]))
async def cmd_howgp(Client, message):
    try:
        user_id = str(message.from_user.id)
        texta = f"""<b>
FREE VS PREMIUM VS PAID

➔ STRIPE AUTH GATE (/au)
  ● ANTISPAM:
   FREE - 30s
   PREMIUM - 5s
   PAID - 5s

➔ STRIPE MASS AUTH GATE (/mass)
  ● ANTISPAM:
   FREE - 120s
   PREMIUM - 80s
   PAID - 30s

  ● CHECKING LIMIT
   FREE - 8
   PREMIUM - 15
   PAID - 25➔ STRIPE CHARGE GATE (/chk)
  ● ANTISPAM:
   FREE - 30s
   PREMIUM - 5s
   PAID - 5s

➔ STRIPE MASS CHARGE GATE (/mchk)
  ● ANTISPAM:
   FREE - 120s
   PREMIUM - 80s
   PAID - 30s

  ● CHECKING LIMIT
   FREE - 8
   PREMIUM - 15
   PAID - 25

➔ STRIPE MASS AUTH GATE WITH TXT FILE CHECKING (/masstxt)
  ● ANTISPAM:
   FREE - 120s
   PREMIUM - 80s
   PAID - 50s

  ● CHECKING LIMIT
   FREE - 200
   PREMIUM - 1000
   PAID - 1500

➔ STRIPE MASS CHARGE GATE WITH TXT FILE CHECKING (/mchktxt)
  ● ANTISPAM:
   FREE - 120S
   PREMIUM - 80S
   PAID - 50S

  ● CHECKING LIMIT
   FREE - 200
   PREMIUM - 1000
   PAID - 1500

➔ STRIPE SK BASED CHARGE GATE WITH TXT FILE CHECKING (/cvv sk)
  ● ANTISPAM:
   FREE - 120s
   PREMIUM - 80s
   PAID - 50s

  ● CHECKING LIMIT
   FREE - 200
   PREMIUM - 1000
   PAID - 1500

➔ CC SCRAPPER GATE (/scr)
  ● SCRAPING LIMIT
   FREE - 3000
   PREMIUM - 6000
   PAID - 12000

➔ CC GENARATOR WITH LUHN ALGO AND CUSTOM AMOUNT GATE (/gen)
  ● GENARATING LIMIT
   FREE - 2000
   PREMIUM - 4000
   PAID - 10000

➔ STRIPE AUTH GATE (/au)
  ● ANTISPAM:
   FREE - 3
   PREMIUM - 3
   PAID - 3
</b>"""
        await message.reply_text(texta, message.id)
        await plan_expirychk(user_id)

    except:
        import traceback
        await error_log(traceback.format_exc())

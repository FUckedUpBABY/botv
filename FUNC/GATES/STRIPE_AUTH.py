import traceback
import random
async def create_auth(fullcc , sks , session,mode):
    try:
        max_amt = 0
        sk = random.choice(sks)
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = splitter[3]
        url1 = "https://api.stripe.com/v1/payment_methods"
        headers1 = {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/payment_methods",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "authorization": f"Bearer {sk}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }
        data1 = f"type=card&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[cvc]={cvv}"
        while True:
            r1 = await session.post(url1, data=data1, headers=headers1)
            result1 = r1.text
            if max_amt == 50 and mode == "1":
                return result1
            if "Request rate limit exceeded." in result1:
                max_amt += 1
                continue
            else:
                break
        try:
            id = r1.json()["id"]
        except:
            return result1
        url2 = "https://api.stripe.com/v1/customers"
        headers2 = {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/customers",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "authorization": f"Bearer {sk}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        }
        data2 = f"description=donation&payment_method={id}"
        while True:
            r2 =await session.post(url2, data=data2, headers=headers2)
            result2 = r2.text
            if max_amt == 50 and mode == "1":
                return result2
            if "Request rate limit exceeded." in result2:
                max_amt += 1
                continue
            else:
                break
        try:
            r2.json()["id"]
            return "succeeded"
        except:
            return result2
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        return str(e)
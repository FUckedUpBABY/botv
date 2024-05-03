import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status   = "Dead 🔴"
            response =  result
            hits     = "NO"

        elif (
            "SUCCESS" in result.text or
            "ThankYou" in result.text or
            "thank_you" in result.text or
            "classicThankYouPageUrl" in result.text
        ):
            status   = "Live 🟢"
            response = "Charged 10$ 🔥"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif "insufficient_funds" in result.text or "card has insufficient funds." in result.text:
            status   = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif (
            "INCORRECT_CVC" in result.text
            or "INVALID_CVC" in result.text
            or "Your card's security code is incorrect." in result.text
        ):
            status   = "Live 🟡"
            response = "INCORRECT_CVC ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif "transaction_not_allowed" in result.text:
            status   = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif '"cvc_check": "pass"' in result.text:
            status   = "Live 🟢"
            response = "CVV LIVE ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif (
            "CompletePaymentChallenge" in result.text
            or "stripe/authentications" in result.text
            or "3d_secure_2" in result.text
        ):
            status   = "Live 🟡"
            response = "3D Challenge Required ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif "stripe_3ds2_fingerprint" in result.text:
            status   = "Live 🟡"
            response = "3D Challenge Required ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif "Your card does not support this type of purchase." in result.text:
            status   = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Shopify Charge 10$", response)

        elif "ProxyError" in result.text:
            status   = "Dead 🔴"
            response = "Proxy Connection Refused 🚫"
            hits     = "NO"
            await refundcredit(user_id)
        else:
            status   = "Dead 🔴"
            response = result.text + " 🚫"
            hits     = "NO"
            try:
                with open("result.text_logs.txt", "a") as f:
                    f.write(fullcc + " - " + "Shopify Charge" + " - " + result.text + "\n")
            except:
                pass

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json 

    except Exception as e:
        status   = "Dead 🔴"
        response = str(e) + " 🚫"
        hits     = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json

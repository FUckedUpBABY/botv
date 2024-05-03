import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status   = "Dead 🔴"
            response = result
            hits     = "NO"
        
        elif (
            "succeeded" in result.text
            or "thank you" in result.text
            or "Thank you" in result.text
            or "Thank You" in result.text
            or "Thank You!" in result.text
            or "Thank you!" in result.text
            or "thank You!" in result.text
            or "thank you!" in result.text
            or "Thank you for your order" in result.text
            or "Thank You for your order" in result.text
            or "Thank You For Your Order" in result.text
            or "Thank you for your order!" in result.text
            or "Thank You for your order!" in result.text
            or "Thank You For Your Order!" in result.text
            or "Thank you for your order." in result.text
            or "Thank You for your order." in result.text
            or "Thank You For Your Order." in result.text
            or "Thank you for your order," in result.text
            or "Thank You for your order," in result.text
            or "Thank You For Your Order," in result.text
            or "Thank you for your order!" in result.text
            or "Thank You for your order!" in result.text
            or "Thank You For Your Order!" in result.text
            or "Thank you for your order," in result.text
            or "Thank You for your order," in result.text
            or "Thank You For Your Order," in result.text
            or "success:true" in result.text
        ):
            status   = "Live 🟢"
            response = "Charged 1$ 🔥"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif "insufficient_funds" in result.text or "card has insufficient funds." in result.text:
            status   = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif (
            "incorrect_cvc" in result.text
            or "security code is incorrect." in result.text
            or "Your card's security code is incorrect." in result.text
        ):
            status   = "Live 🟡"
            response = "CCN Live ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif "transaction_not_allowed" in result.text:
            status   = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif '"cvc_check": "pass"' in result.text:
            status   = "Live 🟢"
            response = "CVV LIVE ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif (
            "three_d_secure_redirect" in result.text
            or "card_error_authentication_required" in result.text
        ):
            status   = "Live 🟡"
            response = "3D Challenge Required ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif "stripe_3ds2_fingerprint" in result.text:
            status   = "Live 🟡"
            response = "3D Challenge Required ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif "Your card does not support this type of purchase." in result.text:
            status   = "Live 🟡"
            response = "Card Doesn't Support Purchase ❎"
            hits     = "YES"
            await forward_resp(fullcc, "Stripe CVV Charge 1$", response)

        elif (
            "generic_decline" in result.text
            or "You have exceeded the maximum number of declines on this card in the last 24 hour period."
            in result.text
            or "Card has been declined, please check your card details and try again" in result.text
        ):
            status   = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits     = "NO"

        elif "do_not_honor" in result.text:
            status   = "Dead 🔴"
            response = "Do Not Honor 🚫"
            hits     = "NO"

        elif "fraudulent" in result.text:
            status   = "Dead 🔴"
            response = "Fraudulent 🚫"
            hits     = "NO"

        elif "setup_intent_authentication_failure" in result.text:
            status   = "Dead 🔴"
            response = "setup_intent_authentication_failure 🚫"
            hits     = "NO"

        elif "invalid_cvc" in result.text:
            status   = "Dead 🔴"
            response = "invalid_cvc 🚫"
            hits     = "NO"

        elif "stolen_card" in result.text:
            status   = "Dead 🔴"
            response = "Stolen Card 🚫"
            hits     = "NO"

        elif "lost_card" in result.text:
            status   = "Dead 🔴"
            response = "Lost Card 🚫"
            hits     = "NO"

        elif "pickup_card" in result.text:
            status   = "Dead 🔴"
            response = "Pickup Card 🚫"
            hits     = "NO"

        elif "incorrect_number" in result.text:
            status   = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits     = "NO"

        elif "Your card has expired." in result.text or "expired_card" in result.text:
            status   = "Dead 🔴"
            response = "Expired Card 🚫"
            hits     = "NO"

        elif "intent_confirmation_challenge" in result.text:
            status   = "Dead 🔴"
            response = "intent_confirmation_challenge 🚫"
            hits     = "NO"

        elif "Your card number is incorrect." in result.text:
            status   = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits     = "NO"

        elif (
            "Your card's expiration year is invalid." in result.text
            or "Your card's expiration year is invalid." in result.text
        ):
            status   = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"
            hits     = "NO"

        elif (
            "Your card's expiration month is invalid." in result.text
            or "invalid_expiry_month" in result.text
        ):
            status   = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"
            hits     = "NO"

        elif "card is not supported." in result.text:
            status   = "Dead 🔴"
            response = "Card Not Supported 🚫"
            hits     = "NO"

        elif "invalid_account" in result.text:
            status   = "Dead 🔴"
            response = "Dead Card 🚫"
            hits     = "NO"

        elif (
            "Invalid API Key provided" in result.text
            or "testmode_charges_only" in result.text
            or "api_key_expired" in result.text
            or "Your account cannot currently make live charges." in result.text
        ):
            status   = "Dead 🔴"
            response = "stripe error . contact support@stripe.com for more details 🚫"
            hits     = "NO"

        elif "Your card was declined." in result.text or "card was declined" in result.text:
            status   = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits     = "NO"

        elif "Payment Intent Creation Failed 🚫" in result.text:
            status   = "Dead 🔴"
            response = "Payment Intent Creation Failed 🚫"
            hits     = "NO"
            await refundcredit(user_id)

        elif "ProxyError" in result.text:
            status   = "Dead 🔴"
            response = "Proxy Connection Refused 🚫"
            hits     = "NO"
            await refundcredit(user_id)

        else:
            status = "Dead 🔴"
            response = await find_between(result.text , "Card has been declined, please check your card details and try again ", ".")
            if response is None:
                response = "Card Declined"
                await result_logs(fullcc, "Stripe Charge", result)
            response = response + " 🚫"
            hits = "NO"

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

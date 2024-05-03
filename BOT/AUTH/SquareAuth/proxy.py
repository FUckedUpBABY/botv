import requests
import random

def proxyset():
    retry = 0
    while retry < 6:
        while retry < 6:
            web = {
                1: '9x8s1ne2aw20aw0nuzh8ukmkwx6lhbsjgdpocyn9',
                2: 'l5q9icmq2de1phcgmuvz1jemt3u4ahtidgmmnft0',
                3: 'o4i7y8o1odyxnrwd87z2iqhhh1sqw9izr35qixnf',
                4: 'tqn18yjc7zyzj35661agucigr2xudwbpy95y1ug1',
                5: 'peu1s5sy0ai5z5m7a2ze7b2tqnf1yqqrxf5go1mn',
                6: 'w4pfoqux5ihgdfdv9rx8996apyjcanft3hq7mlho',
                7: '9285eb5tf9ufyx9okbf507abilyo4w8w89nl6hi6',
                8: 'f30t8bb94of7ce2sho6jr8dtstnnnobokx35jioe',
                9: 'xeudigd9b4v71lcsjxuoqy41ppvha1mtfzoppvhu',
                10: 'fx366ia66nxhggv5npwjc6sellspo5cr6pr3tv8k',
                11: 'hsnjhktsq2vteqtp6fujd6sp34reb99e3ppjlzhx',
                13 : 'lm2eyyla30lmxmemz0dufu19eard1ciruwtxg1mr',
                12 : 'kjof0g5m9r7leattie00pong0o08gx0yji5lb2bo',
                13 : 'sbbw5h1lrlt1ujx74rgmo3fwdyzlholpa83dw6te'
            }

            share = random.choice(list(web.keys()))
            webshare_token = web[share]

            prox = requests.get('https://proxy.webshare.io/api/proxy/list/', headers={'Authorization': f'Token {webshare_token}'})
            prox_res = prox.json()


            if 'count' in prox_res and prox_res['count'] > 0:
                break
            else:
                retry += 1
                continue

        if retry >= 4:
            # print("Failed to retrieve a valid proxy list.")
            break

        count = prox_res['count']
        random_proxy_index = random.randint(0, count - 1)

        proxy_ip = prox_res['results'][random_proxy_index]['proxy_address']
        proxy_port = prox_res['results'][random_proxy_index]['ports']['socks5']
        proxy_user = prox_res['results'][random_proxy_index]['username']
        proxy_pass = prox_res['results'][random_proxy_index]['password']

        proxy = f'socks5://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}'


    return proxy

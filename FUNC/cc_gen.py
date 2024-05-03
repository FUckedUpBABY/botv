async def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord("0")
        if isSecond == True:
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if nSum % 10 == 0:
        return True
    else:
        return False


async def cc_genarator(cc , mes , ano , cvv):
    cc , mes , ano , cvv = str(cc) , str(mes) , str(ano) , str(cvv)
    import random
    if mes != "None" and len(mes) == 1:
        mes = "0" + mes

    if ano != "None" and len(ano) == 2:
        ano = "20" + ano

    numbers = list("0123456789")
    random.shuffle(numbers)
    result = "".join(numbers)
    result = cc + result

    if cc[0] == "3":
        cc = result[0:15]
    else:
        cc = result[0:16]

    if mes == "None":
        mes = str(random.randint(1, 12))
        if len(mes) == 1:
            mes = "0" + str(mes)
    else:
        mes = mes

    if ano == "None":
        ano = random.randint(2024, 2035)
    else:
        ano = ano

    if cvv == "None":
        if cc[0] == "3":
            cvv = str(random.randint(1000, 9999))
        else:
            cvv = str(random.randint(100, 999))
    else:
        cvv = cvv

    return f"{cc}|{mes}|{ano}|{cvv}"



async def luhn_card_genarator(cc , mes , ano , cvv , amount):
    all_cards = ""
    for _ in range(amount):
        while True:
            result = await cc_genarator(cc , mes , ano , cvv)
            ccx , mesx , anox , cvvx = result.split("|")
            check_luhn = await checkLuhn(ccx)
            if check_luhn:
                all_cards += f"{ccx}|{mesx}|{anox}|{cvvx}\n"
                break
    return all_cards

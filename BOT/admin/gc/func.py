from FUNC.usersdb_func import *

def gcgenfunc(len=4):
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(len))


async def insert_pm(gc):
    from mongodb import gcdb
    info = {"gc": gc, "status": "ACTIVE", "type": "PREMIUM"}
    gcdb.insert_one(info)


async def insert_plan1(gc):
    from mongodb import gcdb
    info = {"gc": gc, "status": "ACTIVE", "type": "PLAN1"}
    gcdb.insert_one(info)


async def insert_plan2(gc):
    from mongodb import gcdb
    info = {"gc": gc, "status": "ACTIVE", "type": "PLAN2"}
    gcdb.insert_one(info)


async def insert_plan3(gc):
    from mongodb import gcdb
    info = {"gc": gc, "status": "ACTIVE", "type": "PLAN3"}
    gcdb.insert_one(info)


async def getgc(gc):
    from mongodb import gcdb
    return gcdb.find_one({"gc": gc}, {"_id": 0})


async def getallgc():
    from mongodb import gcdb
    return gcdb.find({}, {"_id": 0})


async def updategc(gc):
    from mongodb import gcdb
    gcdb.update_one({"gc": gc}, {"$set": {"status": "USED"}})


async def plan1gc(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    setkey        = int(get_user_info["totalkey"]) + 1
    usersdb.update_one({"id": user_id} , {"$set": {"totalkey": setkey}})
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id} , {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id} , {"$set": {"plan": "Starter Plan 0.99$ ∞"}})
    getvalidity = str(date.today() + timedelta(days=7)).split("-")
    yy, mm, dd  = getvalidity[0], getvalidity[1], getvalidity[2]
    validity    = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id} , {"$set": {"expiry": validity}})
        

async def plan2gc(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    setkey        = int(get_user_info["totalkey"]) + 1
    usersdb.update_one({"id": user_id} , {"$set": {"totalkey": setkey}})
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id} , {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id} , {"$set": {"plan": "Silver Plan 1.99$ ∞"}})
    getvalidity = str(date.today() + timedelta(days=15)).split("-")
    yy, mm, dd  = getvalidity[0], getvalidity[1], getvalidity[2]
    validity    = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id} , {"$set": {"expiry": validity}})
        


async def plan3gc(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    setkey        = int(get_user_info["totalkey"]) + 1
    usersdb.update_one({"id": user_id} , {"$set": {"totalkey": setkey}})
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id} , {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id} , {"$set": {"plan": "Gold Plan 4.99$ ∞"}})
    getvalidity = str(date.today() + timedelta(days=30)).split("-")
    yy, mm, dd  = getvalidity[0], getvalidity[1], getvalidity[2]
    validity    = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id} , {"$set": {"expiry": validity}})
    


async def onlycredits(user_id):
    usersdb.update_one({"id": user_id} , {"$set": {"status": "PREMIUM"}})
    getuser   = usersdb.find_one({"id": user_id}, {"_id": 0})
    getkey    = int(getuser["totalkey"])
    setcredit = int(getuser["credit"]) + 100
    usersdb.update_one({"id": user_id} , {"$set": {"credit": setcredit}})
    setkey    = getkey + 1
    usersdb.update_one({"id": user_id} , {"$set": {"totalkey": setkey}})

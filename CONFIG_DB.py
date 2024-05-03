import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://asifuzzal775:2NAW1I1gxu7JYTF7@cluster0.s9vuz.mongodb.net"
)

result = str(client)

if "connect=True" in result:
    try:
        print("CONFIG DB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("CONFIG DB CONNECTION FAILED ❌")
    except:
        pass


COLLECTIONS = client["CONFIG_DATABASE"]
BLACKLISTED_SKS = COLLECTIONS.BLACKLISTED_SKS
BLACKLISTED_PKS = COLLECTIONS.BLACKLISTED_PKS
TOKEN_DB = COLLECTIONS.TOKEN_DB
SKS_DB = COLLECTIONS.SKS_DB
PKS_DB = COLLECTIONS.PKS_DB
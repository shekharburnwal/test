import pymongo


client = pymongo.MongoClient("mongodb+srv://skb0387:skb0387@clustertest.xsdz4mu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "Shekhar",
    "email" : "shekharburnwal@gmail.com",
    "age"  : 29
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)
import pymongo
client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.aeiaykn.mongodb.net/?retryWrites=true&w=majority")
db = client.School
collection = db.branches

# CREATE

datas= [
    {
       "name": "CSE",
       "address": "First Floor",
       "teachers": [
           "Divya","Shwetank","Rahul"
       ]
    },
    {
       "name": "ECE",
       "address": "Second Floor",
       "teachers": [
           "Shahu","Rajut"
       ]
    },
    {
       "name": "MECH",
       "address": "Third Floor",
       "teachers": [
           "Shahu","Rajut"
       ]
    }
]
result=collection.insert_many(datas)

# READ

for x in collection.find():
    print(x)
result = collection.find_one({'name':'ECE'})
print(result)

# UPDATE

collection.update_one({'name':'ECE'},{'$set':{'address':'Ground Floor'}})

# DELETE

collection.delete_one({'name':'CSE'})
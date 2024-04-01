import pymongo
import datetime
from bson.objectid import ObjectId  # for strings to ObjectId conversion used in webapp

client = pymongo.MongoClient()
db = client.Mydb
collection = db.colleges
collection.delete_many({})
data = {
    "address": {"college": "CURAJ", "building": "B9"},
    "state": "Rajasthan",
    "cuisine": "Italian",
    "grades": {"date": datetime.datetime.utcnow(), "grade": "A", "score": 98},
}
data_many = [
    {
        "address": {"college": "CURAJ", "building": "B9"},
        "state": "Rajasthan",
        "cuisine": "Italian",
        "grades": {"date": datetime.datetime.utcnow(), "grade": "A", "score": 98},
    },
    {
        "address": {
            "college": "CUR",
        },
        "state": "Rajan",
        "cuisine": "I",
        "grades": {"date": datetime.datetime.utcnow(), "grade": "A", "score": 98},
    },
]
collection.insert_many(data_many)
collection.insert_one(data)
print("Inserted 1 document into the collection")
print("Collections Available: ", db.list_collection_names())
for x in collection.find():
    print(x)
print("Total Number of Documents are: ", collection.count_documents({}))
print(
    collection.find_one(
        {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["address", "state", "cuisine", "grades"],
                "properties": {
                    "address": {
                        "bsonType": "object",
                        "required": ["college", "building"],
                    },
                },
            }
        }
    )
)

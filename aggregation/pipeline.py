import pymongo
import json

client = pymongo.MongoClient()
db = client["home"]
collection = db["aggregation"]
datas = [
    {"name": "Bob", "age": 20, "score": 88, "score2": 89},
    {"name": "Alice", "age": 25, "score": 95, "score2": 89},
    {"name": "Carl", "age": 30, "score": 60, "score2": 89},
    {"name": "Carol", "age": 35, "score": 80, "score2": 89},
    {"name": "Cal", "age": 35, "score": 90, "score2": 89},
    {"name": "Carole", "age": 45, "score": 100, "score2": 89},
    {"name": "Rahul", "age": 50, "score": 100, "score2": 89},
    {"name": "Shubh", "age": 55, "score": 102, "score2": 89},
    {"name": "Ranjeet", "age": 60, "score": 101, "score2": 89},
    {"name": "Rakesh", "age": 35, "score": 102, "score2": 89},
    {"name": "Akshay", "age": 70, "score": 140, "score2": 89},
]
collection.insert_many(datas)
result = collection.aggregate(
    [
        {"$match": {"age": 35}},
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "score": {"$avg": {"$sum": ["$score", "$score2"]}},
            }
        },
        {"$sort": {"score": 1}},
    ]
)

with open("./data.json", "a") as f:
    lis = []
    for res in result:
        lis.append({"_id": str(res["_id"]), "name": res["name"], "score": res["score"]})
    f.write(json.dumps(lis))

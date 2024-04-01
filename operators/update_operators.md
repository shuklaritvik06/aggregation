# Update Operators

```json
{
    "$set": "Sets the value of a field in a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $set: { field: \"value\" } })": {}
},
{
    "$unset": "Removes the specified field from a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $unset: { field: \"\" } })": {}
},
{
    "$inc": "Increments the value of a field in a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $inc: { field: 1 } })": {}
},
{
    "$mul": "Multiplies the value of a field in a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $mul: { field: 1 } })": {}
},
{
    "$rename": "Renames a field in a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $rename: { oldField: \"newField\" } })": {}
},
{
    "$min": "Sets the value of a field in a document to the minimum of the existing value and the specified value.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $min: { field: 1 } })": {}
},
{
    "$max": "Sets the value of a field in a document to the maximum of the existing value and the specified value.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $max: { field: 1 } })": {}
},
{
    "$currentDate": "Sets the value of a field in a document to the current date.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $currentDate: { field: true } })": {}
},
{
    "$addToSet": "Adds a value to an array only if it is not already present.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $addToSet: { field: \"value\" } })": {}
},
{
    "$pop": "Removes the first or last item of an array.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $pop: { field: -1 } })": {}
},
{
    "$pull": "Removes all instances of a value from an array.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $pull: { field: \"value\" } })": {}
},
{
    "$push": "Adds a value to an array.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $push: { field: \"value\" } })": {}
},
{
    "$each": "Adds each value of an array to an existing field in a document.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $each: { field: [\"value1\", \"value2\"] } })": {}
},
{
    "$position": "Specifies the position of an element to be updated.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $push: { field: { $each: [\"value1\", \"value2\"], $position: 0 } } })": {}
},
{
    "$sort": "Sorts an array.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $push: { field: { $each: [\"value1\", \"value2\"], $position: 0 } } })": {}
},
{
    "$slice": "Limits the number of elements in an array.",
    "db.collection.updateOne({ _id: ObjectId(\"5e8f8f8f8f8f8f8f8f8f8f8\") }, { $push: { field: { $each: [\"value1\", \"value2\"], $position: 0 } } })": {}
}
```

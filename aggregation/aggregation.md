# Aggregation

```json
{
    "$addFields": {
        "description": "Adds new fields to documents. Similar to $project, but adds new fields to each document.",
        "implementation": "db.collection.aggregate([{ $addFields: { newField: 'value' } }])"
    },
    "$bucket": {
        "description": "Categorizes incoming documents into groups, called buckets, based on a specified expression and boundaries.",
        "implementation": "db.collection.aggregate([{ $bucket: { groupBy: '$field', boundaries: [0, 10, 20], default: 'Other', output: { count: { $sum: 1 } } } }])"
    },
    "$bucketAuto": {
        "description": "Automatically determines the boundaries for buckets based on the distribution of the input data.",
        "implementation": "db.collection.aggregate([{ $bucketAuto: { groupBy: '$field', buckets: 3, output: { count: { $sum: 1 } } } }])"
    },
    "$count": {
        "description": "Counts the number of documents that pass through the pipeline.",
        "implementation": "db.collection.aggregate([{ $count: 'totalCount' }])"
    },
    "$facet": {
        "description": "Processes multiple aggregation pipelines within a single stage.",
        "implementation": "db.collection.aggregate([{ $facet: { facet1: [ { $match: { field: 'value' } } ], facet2: [ { $group: { _id: '$field', count: { $sum: 1 } } } ] } }])"
    },
    "$geoNear": {
        "description": "Performs a geospatial query that returns documents based on their proximity to a given point.",
        "implementation": "db.collection.aggregate([{ $geoNear: { near: { type: 'Point', coordinates: [ -73.9667, 40.78 ] }, distanceField: 'distance', spherical: true, maxDistance: 1000 } }])"
    },
    "$graphLookup": {
        "description": "Performs a recursive search on a collection.",
        "implementation": "db.collection.aggregate([{ $graphLookup: { from: 'collection', startWith: '$field', connectFromField: 'field', connectToField: 'field', as: 'output' } }])"
    },
    "$group": {
        "description": "Groups documents by a specified expression and outputs to the next stage a document for each distinct grouping.",
        "implementation": "db.collection.aggregate([{ $group: { _id: '$field', count: { $sum: 1 } } }])"
    },
    "$limit": {
        "description": "Passes the first n documents unmodified to the pipeline where n is the specified limit.",
        "implementation": "db.collection.aggregate([{ $limit: 10 }])"
    },
    "$lookup": {
        "description": "Performs a left outer join to another collection in the same database to filter in documents from the 'joined' collection for processing.",
        "implementation": "db.collection.aggregate([{ $lookup: { from: 'collection', localField: 'localField', foreignField: 'foreignField', as: 'output' } }])"
    },
    "$match": {
        "description": "Filters the documents to pass only the documents that match the specified condition(s) to the next pipeline stage.",
        "implementation": "db.collection.aggregate([{ $match: { field: 'value' } }])"
    },
    "$merge": {
        "description": "Combines documents from multiple collections into a single collection.",
        "implementation": "db.collection.aggregate([{ $merge: { into: 'newCollection', on: 'field', whenMatched: 'merge', whenNotMatched: 'insert' } }])"
    },
    "$out": {
        "description": "Writes the resulting documents of the aggregation pipeline to a collection.",
        "implementation": "db.collection.aggregate([{ $out: 'outputCollection' }])"
    },
    "$project": {
        "description": "Reshapes each document in the stream, such as by adding new fields, removing existing fields, or including computed fields.",
        "implementation": "db.collection.aggregate([{ $project: { field1: 1, field2: 1, _id: 0 } }])"
    },
    "$redact": {
        "description": "Controls the content of the documents based on information stored in the documents themselves.",
        "implementation": "db.collection.aggregate([{ $redact: { $cond: { if: { $eq: ['$field', 'value'] }, then: '$$DESCEND', else: '$$PRUNE' } } }])"
    },
    "$replaceRoot": {
        "description": "Replaces the input documents with the specified document.",
        "implementation": "db.collection.aggregate([{ $replaceRoot: { newRoot: '$field' } }])"
    },
    "$sample": {
        "description": "Randomly selects a specified number of documents from its input.",
        "implementation": "db.collection.aggregate([{ $sample: { size: 10 } }])"
    },
    "$skip": {
        "description": "Skips a specified number of documents and passes the remaining documents unmodified to the pipeline.",
        "implementation": "db.collection.aggregate([{ $skip: 5 }])"
    },
    "$sort": {
        "description": "Orders the documents based on the specified expressions. 1 ASC 0 DESC",
        "implementation": "db.collection.aggregate([{ $sort: { field: 1 } }])"
    },
    "$sortByCount": {
        "description": "Groups incoming documents based on the value of a specified expression, then computes the count of documents in each distinct group.",
        "implementation": "db.collection.aggregate([{ $sortByCount: '$field' }])"
    },
    "$unionWith": {
        "description": "Combines documents from multiple collections or views into a single stream of documents.",
        "implementation": "db.collection.aggregate([{ $unionWith: 'otherCollection' }])"
    },
    "$unwind": {
        "description": "Deconstructs an array field from the input documents to output a document for each element.",
        "implementation": "db.collection.aggregate([{ $unwind: '$field' }])"
    }
}
```

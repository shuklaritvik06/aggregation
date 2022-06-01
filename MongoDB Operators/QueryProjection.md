# Operators


- `$eq` : Specifies equality condition

```
"name" : {
    "$eq" : "John"
}
```

- `$ne` : Specifies inequality condition

```
"name" : {
    "$ne" : "John"
}
```
- `$gt` : Specifies greater than condition

```
"age" : {
    "$gt" : 30
}
```

- `$gte` : Specifies greater than or equal to condition

```
"age" : {
    "$gte" : 30
}
```

- `$lt` : Specifies less than condition

```
"age" : {
    "$lt" : 30
}
```
- `$lte` : Specifies less than or equal to condition

```
"age" : {
    "$lte" : 30
}
```
- `$in` : Specifies inclusion condition

```
"age" : {
    "$in" : [30, 31, 32]
}
```

- `$nin` : Specifies exclusion condition

```
"age" : {
    "$nin" : [30, 31, 32]
}
```

- `$exists` : Specifies existence condition

```
db.inventory.find( { qty: { $exists: true, $nin: [ 5, 15]}})

```

- `$type` : Specifies type condition

```
"age" : {
    "$type" : "number"
}
```

- `$and` : Specifies logical AND condition

```
"age" : {
    "$and" : [
        { "$gte" : 30 },
        { "$lte" : 40 }
    ]
}
```

- `$or` : Specifies logical OR condition

```
"age" : {
    "$or" : [
        { "$gte" : 30 },
        { "$lte" : 40 }
    ]
}
```

- `$not` : Specifies logical NOT condition

```
"age" : {
    "$not" : { "$gte" : 30 }
}
```

- `$nor` : Specifies logical NOR condition

```
"age" : {
    "$nor" : [
        { "$gte" : 30 },
        { "$lte" : 40 }
    ]
}
```

- `$regex` : Specifies regular expression condition

```
"name" : {
    "$regex" : "^J",
    "$options" : "i"
}
```
- `$text` : Specifies text search condition

```

Find exact word phrase

db.articles.find( { $text: { $search: "\"coffee shop\"" } } )

Exclude a term from search

db.articles.find( { $text: { $search: "coffee -shop" } } )
```

- `$where` : Specifies JavaScript expression condition

```
"age" : {
    "$where" : "this.age > 30"
}
```

- `$mod` : Specifies modulo condition

```
"age" : {
    "$mod" : [ 10, 0 ]  // age % 10 == 0
}
```
- `jsonSchema` : Specifies JSON Schema condition

```
"age" : {
    "$jsonSchema" : {
        "type" : "number",
        "minimum" : 30,
        "maximum" : 40
    }
}
```

- `$size` : Specifies size condition

```
"name" : {
    "$size" : 5  // In simple it means name.length == 5
}
```

- `$all` : Specifies all elements match condition.

```
"relatives" : {
    "$all" : [ "John", "Mary" ]
}
```

- `$elemMatch` : Specifies element match condition.

```
"relatives" : {
    "$elemMatch" : {
        "name" : "John",
        "age" : { "$gte" : 30 }
    }
}
```

- `$expr` : Specifies JavaScript expression condition

```
"age" : {
    "$expr" : {
        "$add" : [ "$age", 10 ]
    }
}
```

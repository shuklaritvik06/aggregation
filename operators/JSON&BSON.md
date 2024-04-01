# JSON And BSON

JSON is a text-based data format that is commonly used for transmitting data over the web. It is a subset of the BSON data format.

BSON is a binary data format that is commonly used for transmitting data over the network. MongoDB uses BSON for all of its data storage to encrypt the data.

JSON Doc ID => _id is a 12 byte hexadecimal number that is used to ensure that the document is unique. 

First 4 bytes are for current timestamp, next 3 bytes are for machine identifier, next 2 bytes are for process id of MongoDB server, and last 3 bytes are for a counter.
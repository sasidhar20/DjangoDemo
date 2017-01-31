from pymongo import MongoClient

client = MongoClient('localhost', 27017)

print(client)

myDb = client.myFirstMB

print(myDb)

myCollection = myDb.countries

print(myCollection)

print(myDb.collection_names())

record_id = myDb.countries.insert({"name" : "USA"})

print(record_id)
#Getting DB Connection from Mongo
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    print(db)
    return db

def add_currency(db):
    db.currency.insert({"name" : "Rupees","Symbol":"Rs"})

def get_currency(db):
    return db.currency.find_one()

if __name__ == "__main__":
    db = get_db()
    add_currency(db)
    print(get_currency(db))
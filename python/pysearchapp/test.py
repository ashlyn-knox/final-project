import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://ashy:uoCXMG1Dn2vDPepA@cluster0.tq1dm.mongodb.net/stackapp?retryWrites=true&w=majority")

db = client["stackapp"]
col = db["forms"]

x = col.find_one()
form_item = list(x)
print(form_item[1])

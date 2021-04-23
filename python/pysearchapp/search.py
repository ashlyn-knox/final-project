# Import modules
import json
from googlesearch import search
import pymongo
from pymongo import MongoClient
# This isn't working properly
from .settings import mongo

# pprint makes the output look better
from pprint import pprint

# # connect to mongodb
cluster= MongoClient(mongo)
db=cluster["stackapp"]
# db=cluster.admin was original code for above
collection = db["forms"]

form_data = collection.find_one()

form_item = list(form_data)

# ## SERVER VARIABLES ### #
framework = {
    "django": 0,
    "flask": 0,
    "express": 0,
    "laravel": 0,
    "rubyonrails": 0,
    "sinatra": 0
}

# ### Frontend VARIABLES ### #
frontend = {
    "jinja": 0,
    "ejs": 0,
    "blade": 0,
    "react": 0,
    "vue": 0,
    "angular":0
}

databases = {
    "nosql": 0,
    "sql": 0
}
# Test input
item_id = form_item[0]
print(item_id)

python = form_item[1]
javascript = form_item[2] 
ruby = form_item[3]
php = form_item[4]

# set to boolean data type for production
if python == True: 
    framework['django'] += 5
    framework['flask'] += 5
    frontend['jinja'] += 1
elif javascript == True:
    framework['express'] += 5
    frontend['ejs'] += 1
    frontend['react'] += 2
    frontend['vue'] += 2
    frontend['angular'] += 2
elif ruby == True:
    framework['rubyonrails'] += 5
    framework['sinatra'] += 5
elif php == True:
    framework['laravel'] += 5
    frontend['blade'] += 1
else:
    print('Error: Items not assigning values')

mature = form_item[5]
scalable = form_item[5] 
fastDev = form_item[7]
realTime = form_item[8] 
machineAi = form_item[9]
microframe = form_item[10]
if mature == True:
    framework['django'] += 2
    framework['rubyonrails'] += 2
if scalable == True:
    framework['django'] += 2
    framework['express'] += 2
if fastDev == True:
    framework['flask'] += 2
    framework['express'] += 2
    framework['sinatra'] += 2
if realTime == True:
    framework['express'] += 2
if machineAi == True:
    framework['django'] += 2
    framework['flask'] += 2
if microframe == True:
    framework['express'] += 2
    framework['flask'] += 2
    framework['laravel'] += 2
    framework['sinatra'] +=2

    # calculate scores and return all values
flexibleData = form_item[11]
structuredData = form_item[12] 
if flexibleData == 'yes':
        databases['nosql'] += 5
if structuredData == 'yes':
        databases['sql'] += 5
# calculate scores and return all values

frameworkQuery = max(framework)
print(frameworkQuery)

frontendQuery = max(frontend)
print(frontendQuery)

databaseQuery = max(databases)
print(databaseQuery)

# Google search server + documentation + tutorial
for item in search(frameworkQuery + databaseQuery, num=4, stop=4, lang="en", pause=2.0):
    print(item)
# # Google search frontend framework + documentation + tutorial
for item in search(frontendQuery + frameworkQuery, num=4, stop=4, lang="en", pause=2.0):
    print(item)

# Google search Database  + documentation + tutorial
for item in search(databaseQuery, num=4, stop=4, lang="en", pause=2.0):
    print(item)

# Google search  query terms together to find stack building tutorials

# Send data to other json file that the node server will pull from to display

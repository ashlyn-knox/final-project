# Import modules
import json
from googlesearch import search
import pymongo
from pymongo import MongoClient
# Environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

MONGO_URI = os.environ.get('MONGO_URI')
mongo = MONGO_URI
# pprint makes the output look better
from pprint import pprint

# connect to mongo atlas
try:
    cluster = MongoClient('mongodb+srv://ashy:uoCXMG1Dn2vDPepA@cluster0.tq1dm.mongodb.net/stackapp?retryWrites=true&w=majority')
except Error as err:
    print("import", err)

# Database access cluser and collection
db=cluster["stackapp"]
collection = db["forms"]
form_data = collection.find_one({})

# make individual items easily accessible
form_item = list(form_data)

# assign values from db to variables
# Python
if form_item[1] != "python":
    print('incorrect named python variable in db data')
else:
    python = form_item[1]
# JavaScript
if form_item[2] != "javascript":
    print('incorrect named javascript variable in db data')
else:
    javascript = form_item[2] 
# Ruby
if form_item[3] != "ruby":
    print('incorrect named ruby variable in db data')
else:
    ruby = form_item[3] 
# PHP
if form_item[4] != "php":
    print('incorrect named php variable in db data')
else:
    php = form_item[4] 
# Mature Libraries
if form_item[5] != "mature":
    print('incorrect named mature variable in db data')
else:
    mature = form_item[5]
# Scalable framework
if form_item[6] != "scalable":
    print('incorrect named mature variable in db data')
else:
    scalable = form_item[6] 
# Fast Development setup
if form_item[7] != "fastDev":
    print('incorrect named fastDev variable in db data')
else:
    fastDev = form_item[7] 
# Real Time Async behaviour
if form_item[8] != "realTime":
    print('incorrect named realTime variable in db data')
else:
    realTime = form_item[8] 
# Machine Learning and AI
if form_item[9] != "machineAi":
    print('incorrect named machineAi variable in db data')
else:
    machineAi = form_item[9] 
# Microframework
if form_item[10] != "microframe":
    print('incorrect named microframe variable in db data')
else:
    microframe = form_item[10] 
# NoSQL
if form_item[11] != "flexibleData":
    print('incorrect named flexibleData variable in db data')
else:
    flexibleData = form_item[11]
# SQL
if form_item[12] != "structuredData":
    print('incorrect named structuredData variable in db data')
else:
    structuredData = form_item[12] 

# ANALYSIS: Backend variables
framework = {
    "django": 0,
    "flask": 0,
    "express": 0,
    "laravel": 0,
    "rubyonrails": 0,
    "sinatra": 0
}

# ANALYSIS: Frontend Variables
frontend = {
    "jinja": 0,
    "ejs": 0,
    "blade": 0,
    "react": 0,
    "vue": 0,
    "angular": 0
}

# ANALYSIS: Database Variables. TODO Expand for more specific inquery later
databases = {
    "nosql": 0,
    "sql": 0
}

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

if flexibleData == 'yes':
        databases['nosql'] += 5
if structuredData == 'yes':
        databases['sql'] += 5

# calculate scores and return all values
frameworkQuery = max(framework)
frontendQuery = max(frontend)
databaseQuery = max(databases)

# Google search server + database + tutorial
for item in search(frameworkQuery + "webdev", num=5, stop=5, lang="en"):
    print(item)

# # Google search frontend and backend frameworks together
for item in search(frontendQuery + frameworkQuery, num=5, lang="en"):
    print(item)

# Database Links
for item in search(databaseQuery, num=4, lang="en"):
    print(item)
# Frontend Links
for item in search(frontendQuery, num=4, lang="en"):
    print(item)

# Backend Links
for item in search(frameworkQuery, num=4, lang="en"):
    print(item)

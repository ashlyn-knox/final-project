# Import modules
import json
from googlesearch import search
from pymongo import MongoClient
from settings import mongo
# pprint makes the output look better

from pprint import pprint
# connect to mongodb TODO FIX THIS
client = MongoClient(mongo)
db=client.admin
# print results of server status
serverStatusResults=db.command("serverStatus")
pprint(serverStatusResult)

# Read JSON file for search terms TODO move this to a separate file and then import it for assigning values to queries etc


# ### SERVER VARIABLES ### #
django = 0
flask = 0
express = 0
laravel = 0
rubyonrails = 0
sinatra = 0

# ### DB VARIABLES ### #
nosql = 0
sql = 0

# ### Frontend VARIABLES ### #
jinja = 0
ejs = 0
blade = 0

react = 0
vue = 0
angular = 0
# TODO write code that analyzes the form results here and then put that in a separate file that sends data to here
def languageScore():
    if python == True:
        django += 5
        flask += 5
        jinja += 1
    elif javascript == True:
        express += 5
        ejs += 1
        react += 2
        vue += 2
        angular += 2
    elif ruby == True:
        rubyonrails += 5
        sinatra +=5
    elif php == True:
        laravel += 5
        blade += 1
    else:
        return print('error')
    # calculate scores and return all values

def performanceScore():
    if mature == True:
        django += 2
        rubyonrails += 2
    if scalabe == True:
        django += 2
        express += 2
    if fastDev == True:
        django += 1
        flask += 2
        express += 2
        sinatra += 2
    if realTime == True:
        express += 2
    if machineAi == True:
        django += 2
        flask += 2
    # calculate scores and return all values
def databaseScore():
    if flexibleData == True:
        nosql += 5
    if structuredData == True:
        sql += 5
    # calculate scores and return all values

# Google search server + documentation + tutorial
for item in search(query):
    print(item)
# Google search frontend framework + documentation + tutorial

# Google search Database  + documentation + tutorial

# Google search  query terms together to find stack building tutorials

# Send data to other json file that the node server will pull from to display

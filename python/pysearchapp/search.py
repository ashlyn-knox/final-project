# Import modules
# import json
# from googlesearch import search
# from pymongo import MongoClient
# from settings import mongo
# pprint makes the output look better

# from pprint import pprint
# # connect to mongodb TODO FIX THIS
# client = MongoClient(mongo)
# db=client.admin
# # print results of server status
# serverStatusResults=db.command("serverStatus")
# pprint(serverStatusResult)

# Read JSON file for search terms TODO move this to a separate file and then import it for assigning values to queries etc

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
python = input('Python yes or no: ')
javascript = input('Javascript yes or no: ')
print(javascript)
ruby = input('ruby yes or no: ')
print(ruby)
php = input('php yes or no: ')
print(php)

# set to boolean data type for production
if python == True: 
    framework['django'] += 5
    framework['flask'] += 5
    frontend['jinja'] += 1
elif javascript == 'yes':
    framework['express'] += 5
    frontend['ejs'] += 1
    frontend['react'] += 2
    frontend['vue'] += 2
    frontend['angular'] += 2
elif ruby == 'yes':
    framework['rubyonrails'] += 5
    framework['sinatra'] += 5
elif php == 'yes':
    framework['laravel'] += 5
    frontend['blade'] += 1
else:
    print('ERROR')

# if the user wants to try a new language
# TODO logic: IF any in the language equaption is false, add +3 to it. this should be in the same function

# TODO write code that analyzes the form results here and then put that in a separate file that sends data to here
    # calculate scores and return all values
mature = input('mature framework yes or no: ')
scalable = input('scalable importance yes no')
fastDev = input('fastDev yes no')
realTime = input('Real time function yes no')
machineAi = input('Machinelearning y n')
microframe = input('Do you want a microframework')
if mature == 'yes':
    framework['django'] += 2
    framework['rubyonrails'] += 2
if scalable == 'yes':
    framework['django'] += 2
    framework['express'] += 2
if fastDev == 'yes':
    framework['flask'] += 2
    framework['express'] += 2
    framework['sinatra'] += 2
if realTime == 'yes':
    framework['express'] += 2
if machineAi == 'yes':
    framework['django'] += 2
    framework['flask'] += 2
if microframe == 'yes':
    framework['express'] += 2
    framework['flask'] += 2
    framework['laravel'] += 2
    framework['sinatra'] +=2

    # calculate scores and return all values
flexibleData = input('Flexible data model?')
structuredData = input('structured data?')
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
# for item in search(query):
    # print(item)
# # Google search frontend framework + documentation + tutorial

# Google search Database  + documentation + tutorial

# Google search  query terms together to find stack building tutorials

# Send data to other json file that the node server will pull from to display

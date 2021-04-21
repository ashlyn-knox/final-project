# Import modules
try:
    from googlesearch import search
except ImportError:
    print("no module named 'google' found")
# Test search
query = "the dead weather"

for item in search(query):
    print(item)

# Read JSON file for search terms

# TODO write code that analyzes the form results here and then put that in a separate file that sends data to here

# Google search server + documentation + tutorial

# Google search frontend framework + documentation + tutorial

# Google search Database  + documentation + tutorial

# Google search  query terms together to find stack building tutorials

# Send data to other json file that the node server will pull from to display
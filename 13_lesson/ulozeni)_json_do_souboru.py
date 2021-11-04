import json
import requests

response = requests.get ('https://jsonplaceholder.typicode.com/todos/1')
print (response)
print (response.json())
dictionary = (response.json())


file = open('test.json', 'w')
json.dump (dictionary, file, indent=4)

file.close()

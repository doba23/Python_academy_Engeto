import requests
from requests.exceptions import ConnectionError

response = requests.get('https://api.github.com/user')

# print (response)
try:
    response = requests.get('root.cz')
except requests.exceptions.MissingSchema:
    print("Wrong address?")



try:
    response = requests.get('https://forewerdown.org')
except ConnectionError:
    print("Timeout")


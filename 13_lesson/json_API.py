import csv
import requests

with open ('3.csv', 'w', newline='') as csv_file:
    writer = csv.writer (csv_file)
    print (writer)
    data = ['ds','s','12']
    writer.writerow(data)

response = requests.get ('https://jsonplaceholder.typicode.com/todos/1')
print (response)
print (response.json())


import csv
# print (csv.list_dialects())

with open ('3.csv', 'w', newline='') as csv_file:
    writer = csv.writer (csv_file)
    data = ['ds','s','12']
    writer.writerow(data)

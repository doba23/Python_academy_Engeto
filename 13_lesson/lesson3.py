import csv
fh = open('1.csv')
reader = csv.reader(fh)

print (reader)
print (next(reader))
print (next(reader))
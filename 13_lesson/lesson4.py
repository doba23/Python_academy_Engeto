import csv
fh = open('2.csv')
reader = csv.reader(fh,delimiter=':',)

print (reader)
print (next(reader))
print (next(reader))
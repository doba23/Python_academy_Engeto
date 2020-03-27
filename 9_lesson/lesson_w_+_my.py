file = open('test.txt', 'w+')
print(file.write('This is the first line\nThis is the second line\nThis is the third line'))
print (file.seek(0))

for line in file:
    print (line, end='')

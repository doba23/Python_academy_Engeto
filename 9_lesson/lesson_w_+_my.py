file = open('test.txt', 'w+')
print(file.write('This is the first line\nThis is the second line\nThis is the third line'))
print(file.seek(0))

# obdoba metidy .read()
for line in file:
    print(line, end='')

print()
print(file.seek(0))
print()

# precteni prvniho radku
print(file.readline())
print(file.seek(0))

# ulozeni vsech radku do listu
lines_lst = file.readlines()
print(lines_lst)

file.close()

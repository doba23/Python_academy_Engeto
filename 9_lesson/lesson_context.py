# file = open('test.txt','r')
# print(file.read())
# print(file.tell())

with open('test.txt', 'a') as file:
    print(file.write('\nThis is the last line'))

with open('test.txt','r') as file:
    print(file.read())


# Otevreni
file = open('test.txt', 'w')

# Data pro zapis
data = ['Hello', 'Mr', 'Bob']

# zapis
file.writelines(data)

# zavreni
file.close()

# nove otevreni
file = open('test.txt')

#tisk textu se seznamem
print(file.read())

file.close()

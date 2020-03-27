# otevren souboru
file = open('test.txt')
print (file)

# otevren souboru, absolutni cesta
file = open(r'/home/laptop/PycharmProjects/Python_academy_Engeto/9_lesson/test.txt')
text = file.read()
print (file)
print ('')
print (text)
print ('raw text in test.txt:')
print (repr(text))

file.close()

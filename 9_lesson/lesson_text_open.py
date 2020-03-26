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

# zapisovani do souboru
file = open('test.txt','w')
print (file.write('This is the third line\nThis is the fourth line'))
print (file)
file.close()
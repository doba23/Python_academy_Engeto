string1= 'aoidsf'

for i in enumerate (string1):
    print (i)

string1= 'aoidsf'
index = 0

ref_some_string = string1
for i, letter in enumerate (string1):
    letter = letter.upper()
    print (letter, end=' ')

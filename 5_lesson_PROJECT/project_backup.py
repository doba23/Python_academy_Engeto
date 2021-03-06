# Author : Dominik Bauchner
# def funciton for print 41 hypens
def hypen_row ():
    print (41*'-')

# welcome user, save login
hypen_row()
print('Welcome to the app. Please log in:')
username = input ('USERNAME: ')
password = input ('PASSWORD: ')

# login names
reggistered = {'bob':'123',
'ann' : 'pass123',
'mike' : 'password123',
'liz' : 'pass123' }

# if login sucessful continue main program,
# if not repeat login again and again
index = 1
while index:
    if  reggistered.get(username) == password:
        break
    else:
        print('wrong password')
        username = input('USERNAME: ')
        password = input('PASSWORD: ')

# user chose text to analyse
hypen_row()
print ('We have 3 texts to be analyzed.')
index_of_texts = int (input ('Enter a number btw. 1 and 3 to select:')) -1
hypen_row()

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
# Replace comas and full stops in chosed text. Save as a word list

chosed_text = (TEXTS[index_of_texts]).replace('.','').replace(',','').split()

# count total words
def total_words (text):
    total = 0
    for word in text:
        total += 1
    return (total)

# count titlecase words
def titlecase (text):
    count = 0
    for word in text:
        if word[0].isupper():
            count += 1
    return (count)

# count uppercase words
def uppercase (text):
    count = 0
    for word in text:
        if word.isupper():
            count += 1
    return (count)

# count lowercase words
def lowercase (text):
    count = 0
    for word in text:
        if word.islower():
            count += 1
    return (count)

# count number strings
def number_string (text):
    count = 0
    for word in text:
        if word.isnumeric():
            count += 1
    return (count)

# print all of text analyse

print ('There are', total_words(chosed_text), 'words in selected text.')
print ('There are', titlecase(chosed_text), 'titlecase words.')
print ('There are', uppercase(chosed_text), 'uppercase words.')
print ('There are', lowercase(chosed_text), 'lowercase words.')
print ('There are', number_string(chosed_text), 'numeric strings.')
hypen_row()

# found longest string in chosed_text

longest = ''
for i in chosed_text:
    if len (i) > len (longest):
        longest = i


# count each words

for i in range(1,len(longest)+1,):
    count_words = 0
    one_lenght = str(i) + ' '
    for word in chosed_text:
        if len (word) == i:
            one_lenght += '*'
            count_words += 1
    if not count_words == 0:
        print (one_lenght, count_words)
hypen_row()

# count number strings

def number_count (text):
    count = 0
    for word in text:
        if word.isnumeric():
            count += int (word)
    return (count)
print('If we summed all the numbers in this text we would get:', number_count(chosed_text))
hypen_row()
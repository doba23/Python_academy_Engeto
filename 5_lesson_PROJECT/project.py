# Author : Dominik Bauchner
# def funciton for print 41 hypens
def hypen_row ():
    print (41*'-')

# # welcome user, save login
# hypen_row()
# print('Welcome to the app. Please log in:')
# username = input ('USERNAME: ')
# password = input ('PASSWORD: ')
#
# # login names
# reggistered = {'bob':'123',
# 'ann' : 'pass123',
# 'mike' : 'password123',
# 'liz' : 'pass123' }
#
# # if login sucessful continue main program,
# # if not repeat login again and again
# index = 1
# while index:
#     if  reggistered.get(username) == password:
#         break
#     else:
#         print('wrong password')
#         username = input('USERNAME: ')
#         password = input('PASSWORD: ')

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

count_titlecase = 0
count_uppercase = 0
count_lowercase = 0
count_numeric = 0
number_counted = 0
longest = ''
word_len = []

for word in chosed_text:
    # found longest word
    if len (word) > len (longest):
        longest = word
    # append words lenght for next use
    word_len.append(len(word))
    # count titlecase words
    if word[0].isupper():
        count_titlecase += 1
    # count uppercase words
    if word.isupper():
        count_uppercase += 1
    # count lowercase words
    if word.islower():
        count_lowercase += 1
    # count number strings
    if word.isnumeric():
        count_numeric += 1
    #count total number value
        number_counted += int(word)

# print all of text analyse

a = 'There are'
print ('{} {} words in selected text.'.format (a, total_words(chosed_text)))
print ('{} {} titlecase words.'.format(a, count_titlecase))
print ('{} {} uppercase words.'.format(a, count_uppercase))
print ('{} {} lowercase words.'.format(a, count_lowercase))
print ('{} {} number strings.'.format(a, count_numeric))
hypen_row()

# count each words occurance

for i in range(1,len(longest)+1,): # outer iteration print rows based on lenghts of words (until range reaches lenght of longest word)
    count_words = 0 # count quantity of one lenght of word
    one_lenght = str(i) + ' ' # same scheme for each iteration
    for number in word_len: # inner iteration - print occurance of one lenght word
        if number == i: # if lenght of word is same like number of outer iteration do next steps
            one_lenght += '*' # add one star
            count_words += 1 # addition one
    if count_words != 0: # print only word occurances with non zero lenghts
        print (one_lenght, count_words)

hypen_row()

# count number strings
print('If we summed all the numbers in this text we would get:', number_counted)
hypen_row()

# try another solution of word count, unused
# sort word lenght list
word_len.sort()
# hold sequence of unique list items
word_sequence = list(set(word_len))
# count quantity of each word lenght

text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

text = text.replace ('.', '')
text = text.replace (',', '')
text_split = text.split()

search_word = input('input please:')
position = 0

for word in text_split:
    if search_word == word:
        print ('SEARCH OWRD:', word)
        print ('POSITION', position)
    position = position + 1
else :
    print ('NO SUCH A WORD', search_word)

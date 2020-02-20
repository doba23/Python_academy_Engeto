words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

# 1.
max_word = ('',0)

while words:
    # 2.
    word = words.pop(0)
    # 3.
    if len(word) > max_word[1]:
        # 4.
        max_word = word, len(word)
# 5.
print(max_word)

'''
#not sorted dictioanary
#copy list
words_2 = words.copy()
#count word_lenghts
words_lenght = []
while words:
    words_lenght.append(len(words[0]))
    words = words [1:]
#assign words and it's lenght
#to non-sorted dictioanry
words_with_lenght = {}
while words_lenght:
    words_with_lenght[words_lenght[0]] = words_2[0]
    words_lenght = words_lenght [1:]
    words_2 = words_2 [1:]

print (words_with_lenght)

'''
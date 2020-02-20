words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
word = ''
longest_word = ''

while words:
    word = words.pop()
    if len(word) > len(longest_word):
        longest_word = word

print((longest_word + '', len(longest_word)))
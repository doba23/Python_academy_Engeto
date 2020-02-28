sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
sentence = sentence.replace(' ','')
sentence = sentence.replace('.','')
sentence = sentence.lower()
# print (sentence)

vowel_count = 0
cons_count = 0
for i in sentence:
    if i in ['a','e','i','o','u','y']:
        vowel_count += 1
    else:
        cons_count += 1

print('No. consonants:', cons_count, '| No. vowels:', vowel_count)

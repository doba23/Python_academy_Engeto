sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
sentence = sentence.replace(' ','')
sentence = sentence.lower()
print (sentence)

vowel_count = 0
cons_count = 0
for i in sentence:
    print (i)
    if i == ('a' or 'e' or 'i' or 'o' or 'u' or 'y'):
        vowel_count += 1
        print ('if')
        print ('')
    else:
        cons_count += 1
        print('else')
        print('')
print('No. consonants:', cons_count, '| No. vowels:', vowel_count)

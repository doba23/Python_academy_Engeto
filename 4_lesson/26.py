sentence = input('Enter the string:')
# test sentence when programming, now replaced with insertion
# sentence = 'I do not want to work today'
sentence = sentence.split(' ')
repetitions = int(input('Enter the # of repetitions:'))

# auxiliary variables
sentence_echoed = []
index = 0

while sentence:
    slovo = (sentence[0] + ' ')* repetitions
    sentence_echoed.insert(index, slovo)
    sentence = sentence[1:]
    index += 1

# text correction
sentence_echoed = str(sentence_echoed)
sentence_echoed = sentence_echoed.replace ('\'', '')
sentence_echoed = sentence_echoed.replace (' ,', '')
sentence_echoed = sentence_echoed.replace ('[', '')
sentence_echoed = sentence_echoed.replace (']', '')
print (sentence_echoed)



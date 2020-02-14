text = 'This is SenTence.'
index = 0

while index < len(text):
    if text[index].isupper():
        print ('I found cappital letter:'+'\''+ text[index]+'\'')
    index += 1
text = 'This iS SenTence.'

while text:
    if text[0].isupper():
        print('I found cappital letter:' + '\'' + text[0] + '\'')
    text = text[1:]
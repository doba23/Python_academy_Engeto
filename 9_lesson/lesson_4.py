n = input('Your First Name: ')
s = input('Your Surname: ')
e = 'This is an extra sentence. '
greeting = '{extra}Nice to meet you {surname}, {name}.'

print(greeting.format(name=n,extra=e,surname=s))
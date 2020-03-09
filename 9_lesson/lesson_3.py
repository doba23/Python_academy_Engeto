name = input('Your First Name: ')
surname = input('Your Surname: ')
extra = 'This is an extra sentence. '
greeting = '{2}Nice to meet you {1}, {0}.'

print(greeting.format(name,surname,extra))
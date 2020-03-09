name = input('Whats your name?')
age = int (input ('How old are you?'))

print ('My name is %s. I am %d year old.' %(name, age))

fomated_string = 'My name\'s %s. I\'am %d yaer old.'
reference = (name, age)
print(fomated_string % reference)
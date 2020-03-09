#muzeme pouzivat cisla v stringu bez prevadeni s pouzitim techto metod!!

name = input('Whats your name?')
age = int (input ('How old are you?'))

print ('My name is %s. I am %d year old.' %(name, age))

#Formating expression


fomated_string = 'My name\'s %s. I\'am %d yaer old.'
reference = (name, age)
print(fomated_string % reference)

#formating method

formated_method = 'My name is {}. I am {} year old.'.format(name, age)
print (formated_method)

formated_method = 'My name is {1}. I am {0} year old.'.format(age, name)
print (formated_method)

# new python method

new_method = f'My name\'s {name}. I\'m {age} years old'
print(new_method)
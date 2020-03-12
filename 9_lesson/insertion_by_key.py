person_data= {'name':'Dominik', 'age':'28'}

print_it = 'My name is %(name)s. I am %(age)s year old.' % person_data
print (print_it)


print_it2 = 'My name\'s {name}. I \'m {age} year old'.format(name ='Dominik', age = 28)
print(print_it2)

formatted = 'My name is {name}. I am {age} years old'.format(**person_data)
print (formatted)

data = ('Dominik',29)
formatted_2 = 'My name\'s {}. I\'m {} years old'.format(*data)
print (formatted_2)
data= {'name':'Dominik', 'age':'28'}
print_it = 'My name is %(name)s. I am %(age)s year old.' % data
print (print_it)

data= {'name':'Dominik', 'age':'28'}
print_it2 = 'My name\'s {name}. I \'m {age} year old'.format(name ='Dominik', age = 28)
print(print_it2)
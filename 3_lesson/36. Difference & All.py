string01 = 'Bratislava'
string02 = 'Budapest'
different = set(string01).symmetric_difference(set(string02))
all_char =  set(string01).union(set(string02))

print ('{}{}'.format ('Different characters:'.ljust(25), different))
print ('{}{}'.format('All characters:'.ljust(25), all_char))
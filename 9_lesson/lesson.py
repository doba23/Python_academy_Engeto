data = [['Company',     'Date',      'Amount'],
        ['Food Store', '2017-08-01',  -112.56],
        ['Gasoline',   '2017-08-01',  -655.605],
        ['Energy',     '2017-08-07',  -1001.293],
        ['Shoes&CO',   '2017-08-09',  -2130.321],
        ['Electro',    '2017-08-15',  -1566.932],
        ['Mother',     '2017-08-22',   5000.00]]

row_template = '| {:8} | {:8} | {:8} |'

print (row_template.format(**data))













# city = input('What city do you live in? ')
# size = int(input('How many people live in your city? '))
# how = 'big' if size > 1000 else 'small'
# when = 1
#
# print('If there are %d people living in %s, the %s it is %d city' %(size,city,how,when))
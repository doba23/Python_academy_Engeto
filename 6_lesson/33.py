names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]

for l in range (len(names)-1):
    # print ('outer')
    for i in range (len(names)-1):
        if names [i] < names [i+1]:
            # print (i, 'IF')
            continue
        else:
            new = names [i]
            names[i]= names [i+1]
            names[i+1] = new
            # print (i, 'else')
            # print(names)
print (names)
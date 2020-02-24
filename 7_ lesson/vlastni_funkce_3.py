def sum (names : list):
    total = 0
    for name in names:
        total += len(name)
    print (total)

names  =  ['Ahoj','jak','se', 'mas']

sum(names)
#celkove secteni delky kazdeho retezce

names  =  ['Ahoj','jak','se', 'mas']

def sum (names : list):
    total = 0
    for name in names:
        total += len(name)
    print (total)

sum(names)
def unikatni ():
    a = str (input ('Vloz text: '))
    b = set ()
    for i in a:
        b.add(i)
    return b

print (unikatni())
def radacisel ():
    s = 0
    p = 0
    a = float (input('Zadej cislo: '))
    while a != 333:
        s += a
        p += 1
        a = float (input('Zadej cislo: '))
    v = s / p
    print (v)

radacisel()
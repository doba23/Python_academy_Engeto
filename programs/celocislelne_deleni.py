def zbytek(a, b):
    if a > b:
        while a >= b:
            a -= b
        return a
    else:
        while b >= a:
            b -= a
        return b


a, b = 2, 7

print(zbytek(a, b))

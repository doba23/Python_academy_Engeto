a = int(input())
b = int(input())
S = 0

if a>0:

    while b != 0:
        S = S + a
        b = b - 1

else:
    while b !=0:
        S = S - a
        b = b + 1

print('soucin: ', S)

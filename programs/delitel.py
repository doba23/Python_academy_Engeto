a = int(input())
b = int(input())

if a>b:
    d=b
    # print('delenec je b')
else:
    d=a
    # print('delenec je a')

# v = a % d

if a > b:
    while a % d:
        d = d -1
if b > a:
    while b % d:
        d = d - 1

print (d)
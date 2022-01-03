a = int(input())
b = int(input())

if a>b:
    d=b
    # print('delenec je b')
    while a % d !=0:
        d = d -1
else:
    d=a
    # print('delenec je a')
    while b % d !=0:
        d = d - 1

print (d)
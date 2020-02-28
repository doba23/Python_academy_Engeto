start = int (input ('START:'))
stop = int(input ('STOP:'))
divisor = int (input ('DIVISOR:'))

# start = 3
# stop = 9
# divisor = 3
numbers = []

if not divisor:
    print('Cannot divide by zero')
else:
    for i in range (start, stop+1):
        # print (i)
        if not i % divisor:
            numbers.append(i)
        else:
            continue

    print ('Numbers in range(',start,',',stop, ') divisible by', divisor, ':')
    print (numbers)
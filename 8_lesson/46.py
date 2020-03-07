

def s1 (number):
    total = 0
    for i in range (0,len(number),2):
        total += int(number[i])
    return total
print (s1('61789372994'))


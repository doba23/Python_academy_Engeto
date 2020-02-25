numbers = [6,5,4,3]
#print (numbers)
for l in range (len(numbers)-1):
    # print ('outer')
    for i in range (len(numbers)-1):
        if numbers [i] < numbers [i+1]:
            #print (i, 'IF')
            continue
        else:
            new = numbers [i]
            numbers[i]= numbers [i+1]
            numbers[i+1] = new
            #print (i, 'else')
            #print(numbers)
print (numbers)
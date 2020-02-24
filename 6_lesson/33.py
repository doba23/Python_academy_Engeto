listy = [6,4,3,5]
print (listy)
for l in range (len(listy)-1):
    print ('outer')
    for i in range (len(listy)-1):
        if listy [i] < listy [i+1]:
            print (i, 'IF')
            continue
        else:
            new = listy [i]
            listy[i]= listy [i+1]
            listy[i+1] = new
            print (i, 'else')
            print(listy)
print (listy)
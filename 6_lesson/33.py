listy = [6,4,3,5]
print (listy)
for l in range (len(listy)-2):
    print ('outer')
    for i in range (len(listy)-2):
        if listy [i] < listy [i+1]:
            print (i, 'IF')
            next()
        else:
            new = listy [i]
            listy[i]= listy [i+1]
            listy[i+1] = new
            print (i, 'else')
            print(listy)
print (listy)
selection = [ 0,1,2,3 ]

index = int (input ('What index?'))

print (index)
try:
    print (selection[index])
except IndexError:
    print ("There are only {0} chars".format(len(selection)))


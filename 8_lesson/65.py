
def all_anagrams (*args):
    for item in args:
        #print (item)
        #print (args[0])
        if (set(item)).issubset(set(args[0])):
            bol = True
            #print ('if ')
        else:
            #print ('else')
            bol = False
    return bol

print(all_anagrams ('ship', 'ihps', 'hips','spih'))
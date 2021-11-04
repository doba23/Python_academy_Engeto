last = 54
lst = []
i = 1

while last:  # naplneni listu cisly
    lst.append(i)
    last = last - 1
    i = i + 1

lst_2 = lst

# print (lst)

for a in lst:
    if a <= 1:
        lst.remove(a)  # vyrazeni jednicky z prvocisel
    # elif a == 2:
    #     lst.remove(a)
    #     print(lst)
    n = 0
    print('vnejsi iterace', a)
    for i in lst_2:
        print ('vnitrni iterace',i)
        if (a % i) == 0:
            n = n + 1
            print('delenec:{0:3}, delitel:{1:3}, vyskyt:{2:2}'.format(a, i, n))
            if n > 2:
                lst.remove(i)
                break

print(lst)

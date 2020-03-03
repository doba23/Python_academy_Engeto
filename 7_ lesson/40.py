def my_all (own_list):
    boolean = 1 if (own_list) == '' else 0
    for item in own_list:
        boolean = (bool (item))
        # print(item, boolean)
        if (bool (item)) == 0:
            boolean = 0
    return bool (boolean)
print (my_all(''))

def my_any (my_list):
    boolean_2 = 0 if bool (my_list) == 0 else 1
    # print('Boolean od list' boolean_2)
    if boolean_2 == 1:
        boolean_2 = 0
        # print (boolean_2 == 1, 'second step')
        for item_2 in my_list:
            # print('run of for loop')
            if bool(item_2) == 1:
                boolean_2 = 1
                break
            else:
                continue
    return bool (boolean_2)

print (my_any([0,0]))
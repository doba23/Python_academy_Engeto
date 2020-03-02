def all (own_list):
    boolean = 'False' if own_list != 1 else 'True'

    for item in own_list:
        boolean = (bool (item))
        # print(item, boolean)
        if (bool (item)) == 0:
            boolean = 'False'
            break

    return boolean
# print (all([]))

def any (my_list):
    boolean_2 = 'False' if bool (my_list) == 0 else 'True'
    # print('Boolean od list' boolean_2)
    if boolean_2 == 'True':
        boolean_2 = 'False'
        # print (boolean_2 == 1, 'second step')
        for item_2 in my_list:
            # print('run of for loop')
            if bool(item_2) == 1:
                boolean_2 = 'True'
                break
            else:
                continue
    return boolean_2

# print (any([1,0,1,0,0,1,0]))
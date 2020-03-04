def all_anagrams (args):


    for first_in_list in args:
        first = first_in_list
        break
    print (first)
    for outer_item in args:
        (print('outer item',outer_item))
        # print (args[0])
        if first_in_list == outer_item:
            return True
        else:
            return False
    # for inner_item in outer_item:
    #     print (inner_item)

print(all_anagrams (['ship', 'pish']))
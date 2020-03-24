def change_coins (number):
    numbers_l = [50, 20, 10, 5, 2, 1]
    dict = {}

    for item in numbers_l:
        dict[item] = 0
        while number // item != 0:
            dict[item] += 1
            number -= item
        # deletes empty dict items
        if dict[item] == 0:
            del dict [item]
    return (dict)

print (change_coins(109))
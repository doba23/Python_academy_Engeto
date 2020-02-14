cart = [1.02, 3.45, 6.82,5]
i = 0
cont = True

while cont:
    index = i % 4
    print (cart[index])
    user_input = input('For continue press \'Enter\', for quit press \'q\' ')
    if  user_input == 'q':
        cont = False
    else:
        i = i + 1



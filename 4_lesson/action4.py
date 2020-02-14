cart = [1.02, 3.45, 6.82,5]
i = 0
cont = True

while cont:
    index = i % 4
    print(cart[index])
    answer = input('Press enter to continue or "q" to quit: ')
    if answer == 'q':
        cont = False
    else:
        i = i + 1
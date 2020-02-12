cart = []
index = ()
repeat = True
# while plni list az do poctu 3
while repeat:
    item = float(input('Enter the price: '))
    cart.append(item)

    cont = input('Continue with next price. Press A for continue. Press \'q\' For qiut press ')
    if cont == 'q':
       repeat = False


count = 0
total_price = 0
while count is not len(cart):
    total_price = total_price + cart[count]
    count = count + 1
#    print (total_price)
print(total_price)
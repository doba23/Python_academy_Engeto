cart = []
# while plni list az do poctu 3
while len(cart) < 3:
    item = float(input('Enter the price: '))
    cart.append(item)
# vytiskne kosik
print(cart)

count = 0
total_price = 0
while count is not len(cart):
    total_price = total_price + cart[count]
    count = count + 1
#    print (total_price)

print(total_price)
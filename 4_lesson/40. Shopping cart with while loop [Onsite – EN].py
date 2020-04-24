def empty():
    print('')
def row ():
    print('{}'.format(''.ljust(30,'-')))
# Create the cart
cart = []
# 1a. Adding new prices to the cart - allow 3 prices there

cart.append (input('{}'.format('first item price: '.ljust(30,'.'))))
cart.append (input('{}'.format('second item price: '.ljust(30,'.'))))
cart.append (input('{}'.format('third item price: '.ljust(30,'.'))))


# cart.append(input('{}'.format('first item price:'.zfill(30,""))))
# cart.append((input ('Enter the second price:')))
# cart.append((input ('Enter the third price:')))
# 1b. Adding new prices to the cart - allow infinite adding quit by user
cont = True
while cont:
    cart.append (input('{}'.format('Enter the another price:'.ljust(30,'.'))))
    row ()
    cont = (input('{}{}{}'.format('For quit hit enter <'.ljust(30,'-'),'\n',
                              'for continue press any key:'.ljust(30,))))

# 2a. List the cart's content - list all the prices
empty ()
print('{}'.format('INFO: 2a print'.ljust(30,'.')))
row ()

empty()
print ('{}{}{}'.format('Prices are:'.ljust(30,'.'),'\n',cart))

# 2b. List the cart's content - allow infinite listing quit by user
empty ()
print('{}'.format('INFO: 2b print'.ljust(30,'.')))
row ()

cont = True
while cont:
    empty()
    print('{}{}{}'.format('Prices are:'.ljust(30,'.'), '\n', cart))
    empty()
    cont = (input('{}{}{}'.format('For quit hit enter <'.ljust(30, '-'), '\n',
                                  'for continue press any key:'.ljust(30, ))))

# 3. Calculate the total price
total = 0
total_cart = cart
while total_cart:
    total += int(total_cart[0])
    total_cart = total_cart [1:]

# 4. Print the cart's content
duplicate_cart = cart
item = 1
empty()

while duplicate_cart:
    print ('{}{}{}'.format(item,'. item of cart is: '.ljust(29,'.'),duplicate_cart[0]))
    duplicate_cart = duplicate_cart[1:]
    item += 1

# 5. Print the total price

empty()
row ()
print ('{}{}'.format('total price is:'.ljust(29, '.'), total))
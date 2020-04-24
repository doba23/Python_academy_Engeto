def hyp ():
    print (23*'-')

def equ():
    print(23 * '=')
# Creating the shopping cart

# 1. Ask the user for 3 prices (numbers)
print('Please enter the:')
hyp()
item1 = input('{}'.format('first item price:'.ljust(21)))
item2 = input('{}'.format('second item price:'.ljust(21)))
item3 = input('{}'.format('third item price:'.ljust(21)))

# 2. Add them into a list representing the shopping cart,
lst = []
lst.append(int(item1))
lst.append(int(item2))
lst.append(int(item3))

# 3. Calculate the total price,
total = lst[0]+lst[1]+lst[2]

# 4. Print the cart content and the total price.
hyp()
print('{}{}'.format('First item price is'.ljust(21), item1))
print('{}{}'.format('Second item price is'.ljust(21), item2))
print('{}{}'.format('Third item price is'.ljust(21), item3))
equ()
print('{}{}'.format('Total price is'.ljust(21), total))

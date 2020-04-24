# Creating the shopping cart

# 1. Ask the user for 3 prices (numbers),
item1= input('Enter first item:')
item2= input('Enter second item:')
item3= input('Enter third item:')

# 2. Add them into a list representing the shopping cart,
lst = []
lst.append(item1)
lst.append(item2)
lst.append(item3)

# 3. Calculate the total price,
total = 0
while lst:
    total += int(lst[0])
    lst = lst[1:]

# 4. Print the cart content and the total price.
r='='
print('{}{}{}'.format('First item price', r, item1))
print('{}{}{}'.format('Second item price', r, item2))
print('{}{}{}'.format('Third item price', r, item3))
print('{}{}{}'.format('Total price', r, total))

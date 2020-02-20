number = int (input('Please enter your number:'))
numbers = []

#make list with all values with its exponent
index = 0
while len(numbers) < number:
    numbers.insert(index,((index+1)**(index+1)))
    index += 1
#print(numbers)

# sum each value in list
sum = 0
while numbers:
    one_number = numbers.pop()
    sum = sum + one_number
print('The result is:', sum)

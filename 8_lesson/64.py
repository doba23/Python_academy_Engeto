# Luhn test in Python
# reverse numbers
def reverse_digit(card_number):
    number_reversed = ''
    card_number = str (card_number)
    while card_number:
        number_reversed = number_reversed+card_number[-1]
        card_number = card_number[:-1]
    return number_reversed

reverse = reverse_digit(49927398716)
# print (reverse)

# Sum the odd digits
def s1_func (number):
    total = 0
    for i in range (0,len(number),2):
        total += int(number[i])
    return total
s1 = s1_func(reverse)
# print (s1)

# chose even digits
def even(number):
    even_lst = []
    for i in range(1, len(number), 2):
        even_lst.append(number [i])
    return even_lst
even_lst = (even (reverse))
# print (even_lst)

# multiply each even digit x 2
def multiply (number):
    multiply_lst = []
    for i in number:
        multiply_lst.append(int(i)*2)
    return multiply_lst
multiply_lst = multiply(even_lst)
# print(multiply_lst)

# if there more digits, sum the digits of each multiplication
def sum_digits (number):
    sum_digits_lst = []
    for i in number:
        if int (i) < 10:
            sum_digits_lst.append(i)
        else:
            i = str (i)
            first_digit = int(i[0])
            second_digit = int(i[1])
            sum_digits_lst.append((first_digit)+(second_digit))
    return sum_digits_lst

sum_digits_lst = sum_digits (multiply_lst)
# print (sum_digits_lst)

# sum each digit
def s2_func (number):
    total = 0
    for i in number:
        i = int (i)
        total += i
    return total
s2 = s2_func(sum_digits_lst)
# print (s2)

# sum s1+s2 and save to string
result = str(s1 + s2)

# test result
def luhn_test (a):
    if result[1] == '0':
        print ('True')
    else:
        print ('False')

luhn_test(result)



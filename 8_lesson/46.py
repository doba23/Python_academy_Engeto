def reverse_digit(card_number):
    number_reversed = ''
    card_number = str (card_number)
    while card_number:
        number_reversed = number_reversed+card_number[-1]
        card_number = card_number[:-1]
    return number_reversed

print (reverse_digit(49927398716))

def s1 (number):
    total = 0
    for i in range (0,len(number),2):
        total += int(number[i])
    return total

print (s1(reverse_digit(49927398716)))

def s2 (number):
    total = 0
    final_list = []
    for i in range (1,len(number),2):
        # print (number[i])
        multiply = (int(number [i]))*2
        if multiply < 10:
            final_list.append(multiply)
        else:
            # print ((multiply[0]),'+',(multiply[1]))
            final_list.append(multiply[0]+(multiply[1])
    return final_list

print (s2(reverse_digit(49927398716)))

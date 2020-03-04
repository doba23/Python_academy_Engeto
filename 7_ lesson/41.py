def reverse (my_str):
    my_str = list (my_str)
    reversed = []
    for item in range(len(my_str)):
        reversed.append(my_str.pop())
    return reversed

print (reverse('abcdefgh'))

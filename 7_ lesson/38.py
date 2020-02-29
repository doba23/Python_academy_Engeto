# sequence = 'ioasdfhaons'
def my_min(sequence):
    min = sequence [0]
    for i in sequence [1:]:
        if i < min:
            min = i
    return min

print (my_min('iosdfheons'))

def my_max (sequnece_2):
    max = sequnece_2 [-1]
    for j in sequnece_2 [:-1]:
        # print (j, 'for')
        if j > max:
            # print(j, 'pokud je j vetsi nez max, uloz novy max')
            max = j
    return  max

print (my_max('iozsdfheons'))
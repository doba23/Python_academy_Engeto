# sequence = 'ioasdfhaons'
def my_min(sequence):
    min = sequence [0]
    for i in sequence [1:]:
        if i < min:
            min = i
    return min

print (my_min('iosdfheons'))
# a = 'dfheons'
# print(a[-1])

def my_max (sequnece_2):
    max = sequnece_2 [-1]
    for j in sequnece_2 [:-1]:
        print ('max')
        if max < j:
            max = j
    return  max





print (my_max('iozsdfheons'))
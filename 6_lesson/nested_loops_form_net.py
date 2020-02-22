for number in range(4) :
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    # Inner loop
    for another_number in range(1   ):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))

# task :  Write a Python program to construct the following pattern, using a nested for loop:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(6):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(6,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


for a in range (6):
    # print('outer', a)
    for b in range (a):
        print ('* ', end="")
        # print(print('inner', b))
    print ('')

for c in range (6, 0, -1):
    # print('outer', c)
    for d in range (c):
        print ('* ', end="")
        # print('innner', d)
    print ('')
lenght_of_desk = int (input('Type lenght of desk:'))

# create outer and inner range based on input

for_outer = (lenght_of_desk // 2)
for_inner = for_outer
if (lenght_of_desk % 2) == 1:
    for_outer += 1


print (for_outer)
print (for_inner)
# for i in range(len(lenght_of_desk))
for i in range(6):

    for j in range(for_inner):
        print('* ', end="")
    print('')
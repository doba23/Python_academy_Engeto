lenght_of_desk = int (input('Type lenght of desk:'))
symbol = input ('type symbol: ')

# create outer and inner range based on input

for_outer = (lenght_of_desk // 2)
for_inner = for_outer
if (lenght_of_desk % 2) == 1:
    for_outer += 1
chess = []
for i in range (for_outer):
    chess.append(symbol)
    chess.append(' ')
chess = chess [:lenght_of_desk]
print (chess)


# print (for_outer)
# print (for_inner)

# for i in range(len(lenght_of_desk))
# for i in range(6):
#     print('* ', end="")
#     for j in range(for_inner):
#         print(' *', end="")
#     print('')
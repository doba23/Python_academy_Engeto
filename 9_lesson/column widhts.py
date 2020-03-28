table = [['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
['Conyard, Phil', 'WRINKLESS PLUS', 49, 23.55, 1153.95],
['Bettison, Elnora', 'Doxycycline Hyclate', 59, 23.43, 1382.37],
['Skupinski, Wilbert', 'Metolazone', 51, 43.06, 2196.06],
['McShee, Glenn', 'Claravis', 1, 9.85, 9.85]]


lenght_list = []

for row_first in table[0]:
    lenght_list.append(len (row_first))

for row in table:
    for num, item in enumerate(row):
        # print (num, len(str(item)), item)
        if len(str(item)) > lenght_list[num]:
            lenght_list[num] = len(item)

print ('|{0:8^}|{1:7^}|'.format('COLUMN','WIDTH'))
for col, lenght in enumerate(lenght_list):
    a = col +1
    print (('|{0:^5}{1:>1}|{2:^5}|'.format('COL', a, lenght)))

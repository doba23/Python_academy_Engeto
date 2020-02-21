data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]

total_price = 0

for row in data[1:]:
    # print (total_price)
    total_price = total_price + row [2] * row [3]

print('total price is:',total_price)

total_amount = 0

for n in data [1:]:
    total_amount = total_amount + n[3]
    # print(total_amount)

print('total amount is:',total_amount)

zentiva_amount = 0

for row in data [1:]:
    if row[4] == 'Zentiva':
        zentiva_amount = zentiva_amount + row [3]

print('zentiva amount is:', zentiva_amount)

'''
# muj kod
zentiva_amount = 0
for row in data [1:3]:
    zentiva_amount = zentiva_amount + row [3]
    # print(zentiva_amount)

print('zentiva amount is:', zentiva_amount)


# z lekce kod
d = {}
header = data[0][1:]

for row in data[1:]:
    id = row[0]
    d[id] = {}

    for i,item in enumerate(row[1:]):
        key = header[i]
        d[id].update({key: item})

print(d)

'''
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)

number = int (5)
for i in number:
    i % 2 == 0
    for l in i:
        print ('OK')
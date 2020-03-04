# def finding (sequence, find_string):
#     found = -1
#     index = -1
#     for item in sequence:
#         # print(item, find_string)
#         index += 1
#         if item == find_string:
#             found = index
#         else:
#             # print('else')
#             continue
#     return (found)

# print(finding(['pear', 'apple', (23, 45), 653, {'name': 'John'}], 653))
# tup= ('a',5)
# print (tup[1])

def finding (sequence, find_string):
    found = -1
    for item in enumerate (sequence):
        if item[1] == find_string:
            found = item [0]
        else:
            continue
    return (found)

print(finding(['pear', 'apple', (23, 45), 653, {'name': 'John'}], 'pea'))
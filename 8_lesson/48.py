my_str='''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''
my_str = my_str.replace(',','')
my_list = my_str.split()
# print(my_list)

# colect all_email function
def all_email (my_list):
    emails = []
    for item in my_list:
        # print (item.find('@'))
        if item.find('@') != -1:
            emails.append(item)
    return emails

print (all_email(my_list))


emails = ['tiger123@email.cz', 'cnn@info.com', 'abc@gmail.com', 'b2b@money.fr', 'spam@info.cz.']
numeric_mail_list = set ()
# print (type (numeric_mail_list))
for item in emails:
    #print (item)
    for number in item:
        # print (number)
        if number.isnumeric():
            numeric_mail_list.add(item)
print  (numeric_mail_list)

# pokus o list
# def numeric_mail (all_email):
#     numeric_mail_list = set ()
#     for item in all_email:
#         #print (item)
#         for number in item:
#             # print (number)
#             if number.isnumeric():
#                 numeric_mail_list.add(item)
#
# print  (numeric_mail(all_email(my_list)))


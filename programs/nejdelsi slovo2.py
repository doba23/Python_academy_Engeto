def nejdelsislovo (a):
    delka = 0
    for i in a:
        if len(i)>delka:
            delka=len(i)
            m=i
    return m

b ='Toto je veta na rozbor programem'
lst = b.split(' ')
# print (lst)

nejdelsislovo(lst)
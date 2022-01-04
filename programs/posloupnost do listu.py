def posloupnost_do_listu (oddelovac):
    a = input('zadej cisla po sobe')
    lst = []
    for i in a.split(oddelovac):
        lst.append(float(i))
    return lst

oddelovac = ','
print (posloupnost_do_listu(oddelovac))
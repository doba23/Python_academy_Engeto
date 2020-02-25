def multi (symbol: str, count: int):
    result = (symbol * count)
    return result

print (multi ('*', 20))

def multi_2 (symbol: str, count=10):
    result = (symbol * count)
    return result

print (multi_2 ('se'))

#pokud mam zadanou defaultni honotu paramteru numusim ji pri volani zadavat

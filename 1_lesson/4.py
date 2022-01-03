# Ukladani jmena
jmeno = input ('Zadej jmeno:' )

# Tisk jmena
print ('Ukladam', jmeno, 'do jmeno...')

# Ukladani prijmeni
prijmeni = input ('Zadej prijmeni: ')

# Tisk prijmeni
print ('Ukladam',prijmeni, 'do prijmeni...')

# Vytvoreni a tisk promenne cele_jmeno
cele_jmeno = input ('Zadej cele jmeno:')

# Vytvoreni a tisk promenne delka_jmena
delka_jmena = len(cele_jmeno)
print ('Delka jmena je: ', delka_jmena)

# Tisk ohranicene promenne cele_jmeno

def tisk_nakonci():
    print ('=' * delka_jmena)

tisk_nakonci()
print (cele_jmeno)
tisk_nakonci()
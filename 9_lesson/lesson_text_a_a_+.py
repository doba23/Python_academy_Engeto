# U soubor otevřen7  v tomto módu, může připojit nová data vždy za původní obsah.
# Mód 'a' nepodporuje operaci čtení.

file = open('test.txt', 'a')
print( file.write('\nThis is the eighth line'))

#  mód 'a+' podporuje ctení i psaní

# Zavreni souboru
file.close()

# Znovu otevereme v a+
file = open('test.txt', 'a+')

# Cteni souboru
print( file.read())

# Vraceni na zacatek
print(file.seek(0))

# Znovu cteme
print(file.read())

# Zapis do souboru
print(file.write('\nThis is the ninth line'))

# Vraceni na zacatek
print(file.seek(0))

# Znovu cteme po uprave
print(file.read())


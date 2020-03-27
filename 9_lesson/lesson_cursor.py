# Otevreni relativni cestou - skript se musi nachazet tam, kde soubor!

file = open('test.txt')

# Zjisteni pozice
print(file.tell())

# po přečtení souboru se kurzor přesune na jeho konec
print(file.read())
print(file.tell())

# Otevreni relativni cestou - skript se musi nachazet tam, kde soubor!
file = open('test.txt')
# Vraceni se na zacatek souboru
print( file.seek(0))

# Zjisteni aktualni pozice
print( file.tell())

# Znovu - cteni a tisk obsahu souboru
print( file.read())
print(file.tell())
# Mód 'r+' také umožňuje jak čtení, tak psaní v souboru. Data začínáme zapisovat od první pozice (index 0)

file = open(r'/home/laptop/PycharmProjects/Python_academy_Engeto/9_lesson/test.txt', 'r+')

# Zjisteni a tisk pozice - pro mezeru pouzivame vsude extra prazdny print()
print(file.tell())
print()

# Cteni a tisk obsahu
print(file.read())
print()

# Znovu zjisteni a tisk pozice
print(file.tell())
print()

# Zapis noveho textu
print(file.write('\nThis is the seventh line'))
print()

# Posunuti na index 0
print(file.seek(0))
print()

# Znovu cteni a tisk obsahu
print(file.read())
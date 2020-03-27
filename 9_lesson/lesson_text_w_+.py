# otevre soubor v modu w+
file =open('test.txt', 'w+')

# obsah souboru je funkci smazan
print(file.read())

# zapiseme novy obsah
print( file.write('This is the fifth line\nThis is the sixth line'))

# presuneme kurzor na zacatek
file.seek(0)

# print(file.tell())
print(file.read())

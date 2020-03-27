# Metodou seek jsme vždy posunuli na index 0.

file = open('test.txt')
print(file.read())
# Posun na index 0
print(file.seek(0))
print()

#relativní pozice od začátku souboru

file = open('test.txt')
# Posun na index 5 od zacatku
print(file.seek(5))
print(file.read())
print()

# posunout na konec souboru

file = open('test.txt')
# Posun na konec souboru
print(file.seek(0,2))
print(file.read())


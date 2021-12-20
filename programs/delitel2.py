#pisu novy delitel, pred zkouskou

print ("Program deleni beze zbytku")

delenec = int (input('vloz delenec: '))
delitel = int (input('vloz delitele: '))
vysledek = 0

if delitel > delenec:
    print ("Delitel je vetsi nez delenec, deleni nemuze probehnout")
else:
    while delenec >= delitel:
        delenec = delenec - delitel
        vysledek = vysledek + 1

print ("vysledek je: ", vysledek, "zbytek je: ", delenec )
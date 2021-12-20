vstup = int (input ('vloz cislo pro vypocet faktorialu'))
faktorial = 1

while vstup >= 1:
    faktorial = faktorial * vstup
    vstup = vstup - 1
    # print("vstup je :", vstup)
    # print("faktorial je: ", faktorial)

print ("Faktorial je: ", faktorial)
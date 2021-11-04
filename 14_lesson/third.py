class Clovek:
    def __init__(self, rok_narozeni):
        self.__rok_narozeni = rok_narozeni

    def je_plnolety(self):
        return (2020 - self.__rok_narozeni) >= 18

aneta = Clovek(1991)
pavel = Clovek(2003)

print (aneta.je_plnolety())
print (pavel.je_plnolety())
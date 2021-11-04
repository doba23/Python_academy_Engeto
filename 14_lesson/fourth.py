class Clovek:
    def __init__(self, jmeno: str,  rok_narozeni: int):
        self.__jmeno = jmeno
        self.__rok_narozeni = rok_narozeni

    def vrat_jmeno(self):
        # return self.if __name__ == '__main__':
        return self.__jmeno

    def je_plnolety(self):
        return (2020 - self.__rok_narozeni) >= 18

    # getter
    def vrat_datum_narozeni(self):
        return self.__rok_narozeni

    # setter
    def nastav_datum_narozeni (self, nove_datum):
        self.__rok_narozeni = nove_datum

aneta = Clovek('Aneta', 1991)
pavel = Clovek('Pavel', 2003)



print (aneta.je_plnolety())

vstup = print ( 'Novy vek uzivatele', aneta.vrat_jmeno() )
aneta.nastav_datum_narozeni(vstup) #setter
#another option - use for setter
# aneta.nastav_datum_narozeni(2002)

print (aneta.je_plnolety())
print (aneta.vrat_datum_narozeni()) #getter
# print (pavel.je_plnolety())
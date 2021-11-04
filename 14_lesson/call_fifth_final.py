import fifth_final

class Valecnik ():
    def __init__(self, jmeno: str, kostka: Kostka):
        self.__jmeno = jmeno
        self.__kostka = kostka

    def hod_kostkou(self):
        return self.__kostka.hod_kostkou

if __name__ == '__main__':
    sestistenka = Kostka(6)
    franta = Valecnik ('Franta', sestistenka)
    print (franta.hod_kostkou())

    pepa = Valecnik ('Pepa', 'kostka')
import random

class Kostka:
    def __init__(self, pocet_sten: int): # vytvoreni noveho obejktu, ukladame argumenty do atributu, nutny parametr
        self.muj_pocet_sten = pocet_sten # self zavisi na jeden dany obejkt

    def hod_kostkou(self):
        return random.randint(1, self.muj_pocet_sten)

sestistenka = Kostka (6)
desetistenka = Kostka (10)

print (sestistenka.hod_kostkou())
print (desetistenka.hod_kostkou())
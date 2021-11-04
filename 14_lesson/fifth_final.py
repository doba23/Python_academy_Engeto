import random

class Kostka:
    def __init__(self, pocet_sten):
        self.__pocet_sten = pocet_sten

    def hod_kostkou (self):
        return random.randint (1, self.__pocet_sten)
if __name__ == '__main__':
    sestistenka = Kostka (6)
    destistenka = Kostka (10)

    print ('hody sestistenky')
    for _ in range (3):
        print (sestistenka.hod_kostkou())
    print('\nhody desetitistenky')
    for _ in range (10):
        print (destistenka.hod_kostkou())

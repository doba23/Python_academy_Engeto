import random

print ('Hi there!','\n'
       'I\'ve generated a random 4 digit number for you.', '\n'
       'Let\'s play a bulls and cows game.')

def gen_number ():
       secret = [] # list pro ukladani vygenerovanych cislic

       for i,j in  enumerate (range (4)):
              i = random.randint(0, 9)
              if j == 1: # druhy pruchod iterace
                     while i == secret[0]: # dokud by se vygenerovalo stejne cislo, spusti se genrovani znovu
                            i = random.randint(0, 9)
              if j == 2 : # treti pruchod iterace
                     while i == secret[0] or i == secret [1]: # dokud by se vygenerovalo stejne cislo, spusti se genrovani znovu
                            i = random.randint(0, 9)
              if j == 3 : # ctvrty pruchod iterace
                     while i == secret[0] or i == secret [1] or i == secret [2]: # dokud by se vygenerovalo stejne cislo, spusti se genrovani znovu
                            i = random.randint(0, 9)
              secret.append(i)

       return secret



def user_input ():
       digit = str (input ('Enter a number:'))
       lst_user = []
       for i in digit:
              lst_user.append(int(i))

       return (lst_user)

print (user_input())

print (gen_number())





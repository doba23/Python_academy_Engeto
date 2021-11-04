import sys # systemove informace
import os # prace s cestami, jmeny
import shutil # kopirovani souboru a slozek
# print (sys.path)
# print (sys.platform)

# if (sys.platform) == "linux":
#     path = "/home/laptop/PycharmProjects/Python_academy_Engeto/12_lesson"
# elif sys.platform == "win-32":
#     path = "C:/Users/name/PycharmProjects/Python_academy_Engeto/12_lesson"

# print(__file__)

# cela cesta k souboru
print(os.path.realpath(__file__))

# cela cesta ke slozce
path = os.path.dirname(os.path.realpath(__file__))
print (path)

# vytvoreni slozky a souboru
print(os.path.join(path, 'test_folder', 'test_file'))

# try:
#     os.mkdir('path + test_folder')
# except FileExistsError:
#     print('Slozka jiz existuje, nebude vytvorena')

# print (sys.platform)
# print (os.sep)
# print (shutil)

import sys
import test
test.path
print ()

print ('Name from main: ', __name__)
# print (test.funkc(test.var1,test.var2))

print (test.func(1,2))
if __name__ == "__main__":
    print ('We run this scrtipt itself')
if __name__ == "main":
    print('We run this scrtit as imported')

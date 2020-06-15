import main
print ('ahoj muj text z modulu')
var1 = 52
var2 = 53

print ('Name from module: ', __name__)

def func(v1,v2):
    result = v1 + v2
    return result
def summ(a,b):
    return a+b
if __name__ == "__main__":
    num_a = input ('a')
    num_b = input ('b')
    print (summ(a, b))
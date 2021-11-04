import sys
if __name__ == '__main__':
    print (sys.argv)
    try:
        num1, num2, *rest = sys.argv[1:]
    except:
        ('only 2 args')
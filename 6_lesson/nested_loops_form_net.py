for number in range(4) :
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    # Inner loop
    for another_number in range(1):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
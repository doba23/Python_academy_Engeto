import time
# Definice fce
def timer(func, *args, **kwargs):
    # Zjisteni casu pred vykonem fce
    start_time = time.time()
    # Vykonani fce func
    func(*args, **kwargs)
    # Zjisteni casu vykonani fce

    total_time = time.time() - start_time

    # Vraceni dobu trvani vykonu fce func
    return total_time

def bubble_sort (*args):
    numbers = list (args)
    # print (numbers)
    for l in range(len(numbers) - 1):
        # print ('outer')
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                # print (i, 'IF')
                continue
            else:
                new = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = new
                # print (i, 'else')
                # print(numbers)
    return (numbers)

print( bubble_sort (6,5,4,3))
print (timer (bubble_sort, [6,5,4,3]))

from time import sleep

num_seconds = int(input('How many seconds to you need?: '))

while num_seconds:
    print(num_seconds)
    num_seconds = num_seconds - 1
    if num_seconds > 0:
        sleep(1)
    else:
        print('Time has gone!')
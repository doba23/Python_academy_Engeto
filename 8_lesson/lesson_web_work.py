def divisible_by_range (start, stop, divisor):
    nums = []
    for i in range(start, stop):
        if i % divisor == 0:
            nums.append(i)
    return nums

print (divisible_by_range(4,8,3))
print (divisible_by_range(stop=8,divisor=3,start=4))
nums = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]
even= []
odd = []


while nums:
    if not nums[0] % 2:
        even.append(nums[0])
    else:
        odd.append(nums[0])
    nums = nums [1:]

#print (odd)
#print (even)
#summary even list
sum_even = 0
while even:
    sum_even = sum_even + even[0]
    even = even [1:]
#print (sum_even)

#summary odd list
sum_odd = 0
while odd:
    sum_odd = sum_odd + odd[0]
    odd = odd [1:]
#print(sum_odd)

difference = abs (sum_odd - sum_even)
print ('The difference is:',difference )
# DSA practices

# problem: return the max number
def max_number(nums):
    max_num = nums[0]
    n = len(nums)

    for i in range(1,n):
        if max_num < nums[i]:
            max_num = nums[i]

    return max_num
# print(max_number([1,3,2,11,25]))

# problem: even or odoo:
def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return "odd"
# print(even_or_odd(2))

#problem: sum of elements in the array
def sum_of_array(nums):
    total = 0 
    for num in nums:
        total += num
    return total
print(sum_of_array([1,2,3,4]))


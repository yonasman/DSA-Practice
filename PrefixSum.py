# practice prefix sum
# Problem : Range Sum Query
Queries = [(0, 2), (1, 4), (2, 3)]
arr = [1, 3, 5, 7, 9]
n = len(arr)

prefix_sum = [0] * n
prefix_sum[0] = arr[0]

for j in range(1,n):
    prefix_sum[j] = prefix_sum[j - 1] + arr[j]
# print(prefix_sum)
output = []
for t in Queries:
    if t[0] == 0:
        sum_range = prefix_sum[t[1]]
    else:
        sum_range = prefix_sum[t[1]] - prefix_sum[t[0] - 1]
    output.append(sum_range)
# print(output)
# Problem: Sub array with Given Sum
def subArraySum(nums, target):
    n = len(nums)
    prefix_sum = 0
    hash_map = {0 : 1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - target in hash_map:
            return True
        
        if prefix_sum in hash_map:
            hash_map[prefix_sum] += 1
        else:
            hash_map[prefix_sum] = 0
    return False
    
# print(subArraySum([10, 2, -2, -20, 10], -10))
def maxSumSubArr(nums):
    n = len(nums)
    max_sum = 0
    min_prefix_sum = 0
    current_prefix_sum = 0
    
    for i in range(n):
        current_prefix_sum += nums[i]
        
        max_sum = max(max_sum, current_prefix_sum - min_prefix_sum)
        
        min_prefix_sum = min(min_prefix_sum, current_prefix_sum)
        
    return max_sum
# print(maxSumSubArr([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
def numOfSubArrays(nums,k):
    n = len(nums)
    prefix_sum = 0
    subArrayCount = 0
    prefix_sum_map = {0:1}
    i = 0
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in prefix_sum_map:
            subArrayCount += prefix_sum_map[prefix_sum - k]

        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum] += 1
        else:
            prefix_sum_map[prefix_sum] = 1
    return subArrayCount
# print(numOfSubArrays([1, 2, 3, 4, 5, 6, 7, 8, 9],15))
def runningSum(nums):
    n = len(nums)
    for i in range(1,n):
        nums[i] = nums[i - 1] + nums[i]
    return nums
# print(runningSum([1,2,3,4]))
def runningSum2(nums):
    n = len(nums)
    i = 1
    while i < n:
        nums[i] = nums[i - 1] + nums[i]
        i += 1
    return nums
print(runningSum2([1,2,3,4]))
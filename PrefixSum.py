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
# print(runningSum2([1,2,3,4]))
def largestAltitude(gain):
    n = len(gain)
    altitude = [0] * (n + 1)
    altitude[0] = 0
    altitude[1] = gain[0]
    
    for i in range(2,n+ 1):
        altitude[i] = altitude[i - 1] + gain[i - 1]
    print(altitude)
    return max(altitude)
# print(largestAltitude( [-5,1,5,0,-7]))
def largestAltitude2(gain):
    max_altitude = 0
    current_altitude = 0
    
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude
# print(largestAltitude2([-5,1,5,0,-7]))
def findMiddleIndex(nums):
    n = len(nums)
    leftSum = 0
    totalSum = sum(nums)
    
    for i in range(n):
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1
# print(findMiddleIndex([2,3,-1,8,4]))
def sum_of_all_subarrays(nums):
    n = len(nums)
    totalSum = 0
    
    for i in range(n):
        subArraySum = 0
        for j in range(i,n):
            subArraySum += nums[j]
            totalSum += subArraySum
    return totalSum
# print(sum_of_all_subarrays([1,2,3]))
def sum_of_all_subarrays2(nums):
    n = len(nums)
    totalSum = 0
    
    for i in range(n):
        totalSum += nums[i] * (i + 1) * (n - i)
    return totalSum
# print(sum_of_all_subarrays2([1,2,3]))
def EquilibriumIndex(nums):
    n = len(nums)
    leftSum = [0] * n
    leftSum[0] = nums[0]
    rightSum = [0] * n
    rightSum[n - 1] = nums[n - 1]
    
    for i in range(1,n):
        leftSum[i] = leftSum[i - 1] + nums[i]
        
    for j in range(n - 2, -1, -1):
        rightSum[j] = rightSum[j + 1] + nums[j]
    for i in range(n):
        for j in range(n):
            if i == j and leftSum[i] == rightSum[j]:
                return i
# print(EquilibriumIndex([1, 7, 3, 6, 5, 6]))
def EquilibriumIndex2(nums):
    totalSum = sum(nums)
    leftSum = 0
    n = len(nums)
    
    for i in range(n):
        rightSum = totalSum - leftSum - nums[i]
        if rightSum == leftSum:
            return i
        leftSum += nums[i]
    return -1
# print(EquilibriumIndex2([1, 7, 3, 6, 5, 6]))
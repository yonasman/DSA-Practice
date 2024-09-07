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
def rangeSumQuery(nums,queries):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    
    for i in range(1,n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    
    output = []
    for q in queries:
        if q[0] == 0:
            output.append(prefix_sum[q[1]])
        else:
            current_query = prefix_sum[q[1]] - prefix_sum[q[0] - 1]
            output.append(current_query)
    return output
# print(rangeSumQuery([1, 2, 3, 4, 5], [(1, 3), (2, 4), (0, 4)]))
def count_subarrays_with_sum(nums, target):
        n = len(nums)
        # prefix_sum = [0] * n
        targetSumCount = 0
        
        for i in range(n):
            subArraySum = 0
            for j in range(i,n):
                subArraySum += nums[j]
                if subArraySum == target:
                    targetSumCount += 1
        return targetSumCount
# print(count_subarrays_with_sum([1, 2, 3, 4, 5],9))
[1,3,6,10,19]
def count_subarrays_with_sum2(nums, target):
    target_count = 0
    prefix_sum = 0
    prefix_count_map = {0:1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - target in prefix_count_map:
            target_count += prefix_count_map[prefix_sum - target]
            
        if prefix_sum in prefix_count_map:
            prefix_count_map[prefix_sum] += 1
        else:
            prefix_count_map[prefix_sum] = 1
            
    return target_count
# print(count_subarrays_with_sum2([1,2,3,4,5],9))
def maximumSubArraySum(nums):
    n = len(nums)
    if n == 0:
        return 0
    maxSum = float("-inf")
    
    for i in range(n):
        currentSum = 0
        for j in range(i,n):
            currentSum += nums[j]
            maxSum = max(currentSum, maxSum)
            print(maxSum)
    return maxSum
# print(maximumSubArraySum([1,-3,-5,4,5]))
def maxSubArraySum2(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(current_sum, max_sum)
    return max_sum
# print(maxSubArraySum2([1,-3,-5,4,5]))

def maxSubArraySum3(nums):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    maxSum = float("-inf")
    min_prefix_sum = 0
    
    
    for i in range(1,n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    
    for j in range(n):
        maxSum = max(maxSum, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[j])
    return maxSum
# print(maxSubArraySum3([1,-3,-5,4,5]))
def rangeQuery(nums,queries):
    n = len(nums)
    prefixSum = [0] * n
    prefixSum[0] = nums[0]
    
    for i in range(1,n):
        prefixSum[i] = prefixSum[i - 1] + nums[i]
        
    output = []
    for q in queries:
        if q[0] == 0:
            print(prefixSum[q[1]])
            output.append(prefixSum[q[1]])
        else:
            output.append(prefixSum[q[1]] - prefixSum[q[0] - 1])
    return output
# print(rangeQuery([1, 3, 5, 7, 9],[(1, 3), (0, 4)]))
def equilibriumIndex3(nums):
    n = len(nums)
    totalSum = sum(nums)
    leftSum = 0
    
    for i in range(n):
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1
# print(equilibriumIndex3([-7, 1, 5, 2, -4, 3, 0]))
def subArraySumCountWithTarget(nums, target):
    n = len(nums)
    count = 0
    
    for i in range(n):
        subArraySum = 0
        for j in range(i,n):
            subArraySum += nums[j]
            if subArraySum == target:
                count += 1
    return count
    # time complexity = o(n^2)
    # space complexity = o(1)
# print(subArraySumCountWithTarget([1,1,1],2))
def subArraySumCountWithTarget2(nums,target):
    n = len(nums)
    prefix_sum = 0
    prefix_sum_map = {0:1}
    subArrayCount = 0
    
    for i in range(n):
        prefix_sum += nums[i]
        
        if prefix_sum - target in prefix_sum_map:
            subArrayCount += prefix_sum_map[prefix_sum - target]
            
        if prefix_sum in prefix_sum_map:
            prefix_sum += 1
        else:
            prefix_sum = 1
    return subArrayCount
# print(subArraySumCountWithTarget2([1,1,1],2))
def maxSubArrayWithinTarget(nums, target):
    n = len(nums)
    maxSum = float("-inf")
    
    for i in range(n):
        currentSum = 0
        for j in range(i,n):
            currentSum += nums[j]
            if currentSum <= target:
                maxSum = max(maxSum, currentSum)
    return maxSum if maxSum != float("-inf") else 0
# print(maxSubArrayWithinTarget([2, 1, -3, 4, -1, 2, 1, -5, 4],7))
def maxSubArrayWithinTarget2(nums,target):
    prefix_sum = 0
    prefix_sum_map = {0:0}
    max_sum = float("-inf")
    
    for num in nums:
        prefix_sum += num

        for prev_sum in prefix_sum_map:
            if prefix_sum - prev_sum <= target:
                max_sum = max(max_sum, prefix_sum - prev_sum)
    
    if prefix_sum not in prefix_sum_map:
        prefix_sum_map[prefix_sum] = 0
    return max_sum if max_sum != float("-inf") else 0
# print(maxSubArrayWithinTarget2([2, 1, -3, 4, -1, 2, 1, -5, 4],7))
def subArrayQueries(nums, queries):
    n = len(nums)
    prefix_sum = [0] * (n)
    prefix_sum[0] = nums[0]
    # [0,0,0,0,0,0]
    for i in range(1,n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    output = []
    for L,R in queries:
        L -= 1
        R -= 1
        if L == 0:
            output.append(prefix_sum[R])
        else:
            output.append(prefix_sum[R] - prefix_sum[L - 1])
    return output
# print(subArrayQueries([1, 2, 3, 4, 5],[(1, 3), (2, 5), (1, 5)]))
def prefix_sum2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1,rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i][j-1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]
    
    return prefix_sum
def twoD_prefix_sum(prefix_sum2, r1,c1,r2,c2):
    twoDSum = prefix_sum2[r2][c2] - prefix_sum2[r1-1][c1] - prefix_sum2[r1][c1 -1] + prefix_sum2[r1-1][c1-1]
    return twoDSum
print(twoD_prefix_sum(prefix_sum2([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]),1,1,3,3))
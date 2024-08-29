# practice prefix sum
# Problem : Range Sum Query
Queries = [(0, 2), (1, 4), (2, 3)]
arr = [1, 3, 5, 7, 9]
n = len(arr)

prefix_sum = [0] * n
prefix_sum[0] = arr[0]

for j in range(1,n):
    prefix_sum[j] = prefix_sum[j - 1] + arr[j]

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
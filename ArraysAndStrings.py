# array and string practice
def pivotIndex(nums):
    n = len(nums)
    for i in range(n):
        if(sum(nums[:i]) == sum(nums[i + 1:])):
            return i
    return -1
# print(pivotIndex([1,2,3]))
def pivotIndex2(nums):
    # if nums in empty
    if not nums:
        return -1
    totalSum = sum(nums)
    leftSum = 0
    
    for i,num in enumerate(nums):
        rightSum = totalSum - leftSum - num
        if leftSum == rightSum:
            return i
        leftSum += num
    return -1
print(pivotIndex2([1,2,3]))

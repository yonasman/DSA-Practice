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
# print(pivotIndex2([1,2,3]))
def doubleChar(txt):
    newTxt = ""
    for t in txt:
        newTxt += t * 2
    return newTxt
# print(doubleChar("hello"))
# binary search
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return f"Exists at index {mid}"
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return "The target never Exists"
# print(binarySearch([1,2,3,4,5,6,7,8,9],2))
def twoSum(nums,target):
    n = len(nums)
    p1 = 0
    p2 = 1
    while p1 < n:
        if nums[p1] + nums[p2] == target:
            return [p1,p2]
        elif p2 == n - 1:
            p1 += 1
            p2 = p1 + 1
        else:
            p2 += 1
# print(twoSum([3,2,4],6))
def twoSum2(nums,target):
    nums_dict = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement],i]
        nums_dict[num] = i
    return []
# print(twoSum2([3,2,4],6))
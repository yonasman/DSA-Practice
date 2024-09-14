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
def pivotIndex3(nums):
    leftSum = 0
    totalSum = sum(nums)
    for i,num in enumerate(nums):
        rightSum = totalSum - leftSum - num
        if leftSum == rightSum:
            return i
        leftSum += num
    return -1
# print(pivotIndex3([1,7,3,6,5,6]))
def maxSubArray(nums):
    n = len(nums)
    maxSum = float("-inf")
    for i in range(n):
        currentSum = 0
        for j in range(i,n):
            currentSum += nums[j]
            maxSum = max(maxSum,currentSum)
    return maxSum
# print(maxSubArray([5,4,-1,7,8]))
def maxSubArray2(nums):
    currentSum = nums[0]
    maxSum = nums[0]
    for num in nums[1:]:
        currentSum = max(num, currentSum + num)
        maxSum = max(num, currentSum)
    return maxSum
# print(maxSubArray2([5,4,-1,7,8]))
def reverseString(s):
    n = len(s)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        s[p1],s[p2] = s[p2],s[p1]
        p1 += 1
        p2 -= 1
    print(s)
# # reverseString(["h","e","l","l","o"])
def isPalindrome(s):
    alNum = "abcdefghijklmnopqrstuvwxyz1234567890"
    filtered = [x.lower() for x in s if x.lower() in alNum]
    return filtered == filtered[::-1]
# print(isPalindrome("A man, a plan, a canal: Panama"))
def isPalindrome2(s):
    filtered = ''.join([x.lower() for x in s if x.isalnum()])
    return filtered == filtered[::-1]
# print(isPalindrome2("A man, a plan, a canal: Panama"))
def strStr(haystack,needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1
# print(strStr("leetcode","leeto"))
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    n = len(strs)
    prefix = strs[0]
    for i in range(1,n):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
# print(longestCommonPrefix(strs = ["flower","flow","flight"]))
def longestCommonPrefix2(strs):
    # if strs is empty
    if not strs:
        return ""
    
    n = len(strs)
    for i in range(len(strs[0])):
        prefix = strs[0][i]
        for j in range(1,n):
            # if the length exceeds or mismatch found
            if i >= len(strs[j]) or strs[j][i] != prefix:
                return strs[0][:i]
    return strs[0]
# print(longestCommonPrefix2(["flower","flow","flight"]))
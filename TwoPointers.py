# PRACTICE TWO POINTERS ALGORITHM
def mergeArr(arr1,arr2):
    arr = arr1 + arr2
    return sorted(arr)
# print(mergeArr([1,2,3],[2,2,3]))
# using two pointer
def mergeArr2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    p1,p2 = 0,0
    output = []
    while p1 < n and p2 < m:
        if arr1[p1] <= arr2[p2]:
            output.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            output.append(arr2[p2])
            p2 += 1
    return output
# print(mergeArr2([1,3,9,15,20], [2,4,19,19]))
def find_pair(nums, target):
    n = len(nums)
    left, right = 0,n - 1
    nums.sort()
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left],nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
# print(find_pair([2,3,1,4],4))
def reverse_arr(nums):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
# print(reverse_arr([2,3,1,4]))
def flipAndInvertImage(images):
    n = len(images)
    for image in images:
        left, right = 0, n - 1
        while left <= right:
            image[left],image[right] = 1- image[right],1- image[left]
            left += 1
            right -= 1
    return images
# print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
#[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# reversing an array without using two pointers
def reverse_arr2(nums):
    n = len(nums)
    reversed_arr = [0] * n
    for i in range(n):
        reversed_arr[i] = nums[n - 1 - i]
    return reversed_arr
# print(reverse_arr2([1,1,0,0]))
# apply operations to an array
def apply_operations(nums):
    n = len(nums)
    p1, p2 = 0, 1
    while p2 < n:
        if nums[p1] == nums[p2]:
            nums[p1] = nums[p1] * 2
            nums[p2] = 0
            p1 += 1
            p2 += 1
        else:
            p1 += 1
            p2 += 1
            
    # push zeros
    # output = [0] * n
    # non_zero_idx = 0
    # for i in range(n):
    #     if nums[i] != 0:
    #         output[non_zero_idx] = nums[i]
    #         non_zero_idx += 1
    non_zero_idx = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_idx],nums[i] = nums[i], nums[non_zero_idx]
            non_zero_idx += 1
    return nums
# print(apply_operations([1,2,2,1,1,0]))
def move_zeros(nums):
    n = len(nums)
    non_zero_idx = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
            non_zero_idx += 1
    return nums
# print(move_zeros([0,1,0,3,12]))
def isStrictlyPalindromic(n):
    for base in range(2,n - 1):
        stringRep = ""
        num = n
        while num > 0:
            numStr = num % base
            stringRep = str(numStr) + stringRep
            num //= base
            if stringRep != stringRep[::-1]:
                return False
    return True
# print(isStrictlyPalindromic(9))
def sortColors(colors):
    low, mid, high = 0,0,len(colors) - 1
    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            mid += 1
        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1
            mid += 1
    return colors
# print(sortColors([2,0,2,1,1,0]))
def removeDuplicates(nums):
    n = len(nums)
    output = []
    for num in nums:
        if num not in output:
            output.append(num)
    return len(output)
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
def removeDuplicates2(nums):
    n = len(nums)
    if not nums:
        return 0
    unique_ele = 1
    for i in range(1,n):
        if nums[i] != nums[i - 1]:
            nums[unique_ele] = nums[i]
            unique_ele += 1
    return unique_ele
# print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
def removeDuplicates3(nums):
    if len(nums) == 0:
        return 0
    n = len(nums)
    i = 0
    for j in range(1,n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# print(removeDuplicates3([0,0,1,1,1,2,2,3,3,4]))
def removeElement(nums, val):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
# print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    return haystack.index(needle)
# print(strStr(haystack = "leetcode", needle = "leeto"))
def strStr2(haystack, needle):
    p1, p2 = 0, len(needle)
    n = len(haystack)
    while p1 < n:
        if haystack[p1:p2] == needle:
            return p1
        else:
            p1 += 1
            p2 += 1
    return -1
# print(strStr2(haystack = "leetcode", needle = "leeto"))
def strStr3(haystack, needle):
    if not needle:
        return 0
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i
    return -1
# print(strStr3(haystack = "leetcode", needle = "leeto"))
# valid palindrome
def isPalindrome(s):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    n = len(s)
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if s[p1].lower() not in chars:
            p1 += 1
        elif s[p2].lower() not in chars:
            p2 -= 1
        elif s[p1].lower() != s[p2].lower():
            return False
        else:
            p1 += 1
            p2 -= 1
    return True
# print(isPalindrome(" "))
def isPalindrome2(s):
    filtered = "".join(char.lower() for char in s if char.isalnum())
    return filtered == filtered[::-1]
# print(isPalindrome2("A man, a plan, a canal: Panama"))
def isPalindrome3(s):
    filtered = "".join(filter(str.isalnum,s.lower()))
    p1 = 0
    p2 = len(filtered) - 1
    while p1 < p2:
        if filtered[p1] != filtered[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
# print(isPalindrome3("A man, a plan, a canal: Panama"))
def intersectArr(nums1, nums2):
    nums1.sort()
    nums2.sort()
    p1,p2 = 0,0
    output = []
    n,m = len(nums1), len(nums2)
    while p1 < n and p2 < m:
        if nums1[p1] == nums2[p2]:
            output.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return output
# print(intersectArr(nums1 = [1,2,2,1], nums2 = [2,2]))
def twoSum(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
# print(twoSum(nums = [2,7,11,15], target = 9))
def countPairs(nums, target):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] < target:
                count += 1
    return count
# print(countPairs(nums = [-1,1,2,3,1], target = 2))
def countPairs2(nums, target):
    n = len(nums)
    i,j = 0,1
    count_pair = 0
    while i < n - 1:
        if nums[i] + nums[j] < target:
            count_pair += 1
        j += 1
        if j == n:
            i += 1
            j = i + 1
    return count_pair
# print(countPairs2(nums = [-6,2,5,-2,-7,-1,3], target = -2))
def threeSum(nums):
    nums.sort()
    n = len(nums)
    output = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return output
# print(threeSum(nums = [-1,0,1,2,-1,-4]))
# arithmetic triplets
def dailyTemperatures(temperatures):
    n = len(temperatures)
    p1 = 0
    p2 = 1
    output = []
    while p1 < n and p2 < n:
        print(temperatures[p1], temperatures[p2])
        if temperatures[p1] < temperatures[p2]:
            output.append(p2 - p1)
            p1 += 1
            p2 = p1 + 1 
        elif temperatures[p1] >= temperatures[p2]:
            if p2 == n-1:
                p1 += 1
                p2 = p1 + 1
                output.append(0)
            else:
                p2 += 1
    output.append(0)
    return output
# print(dailyTemperatures([30,60,90]))
def findMaxAverage(nums,k):
    n = len(nums)
    p2 = k
    max_avg = float("-inf")
    for p1 in range(n - k + 1):
        print(sum(nums[p1:p2]))
        current_avg = sum(nums[p1:p2]) / k
        max_avg = max(current_avg, max_avg)
        p2 += 1
    return max_avg
# print(findMaxAverage(nums = [5], k = 1))

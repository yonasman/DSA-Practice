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
def isValidAnagram(str1,str2):
    dict1 = {}
    dict2 = {}
    for s in str1:
        dict1[s] = dict1.get(s,0) + 1
    for s in str2:
        dict2[s] = dict2.get(s,0) + 1
    return dict1 == dict2
# print(isValidAnagram( "rat", "car"))
def validAnagram(s,t):
    if len(s) != len(t):
        return False
    
    counter = {}
    for str in s:
        counter[str] = counter.get(str,0) + 1
    for char in t:
        if char not in counter:
            return False
        counter[char] -= 1
        if counter[char] < 0:
            return False
    return True
# print(validAnagram("rat", "car"))

def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
# print(groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))
def longestSubstring(s):
    if not s:
        return 0
    n = len(s)
    p1 = 0
    p2 = 0
    maxLen = 0
    while p1 < n and p2 < n:
        if s[p2] not in s[p1:p2]:
            maxLen = max(maxLen, p2 - p1 + 1)
            p2 += 1
        else:
            p1 += 1
    return maxLen
# print(longestSubstring("bbbb"))
def longestSubstring2(s):
    if not s:
        return 0
    n = len(s)
    left = 0
    right = 0
    maxLen = 0
    seen = set() #abcb
    while left < n and right < n:
        if s[right] not in seen:
            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            right += 1
        else:
            seen.remove(s[left])
            left += 1
    return maxLen
# print(longestSubstring2("abcabcbb"))
def longestSubstring3(s):
    n = len(s)
    if n == 0:
        return 0
    p1 = 0
    seen = set()
    maxLen = 0
    for p2 in range(n):
        while s[p2] in seen:
            seen.remove(s[p1])
            p1 += 1
        seen.add(s[p2])
        maxLen = max(maxLen, p2 - p1 + 1)
    return maxLen
# print(longestSubstring3("abcabcab"))
def containDuplicates(nums):
    return len(set(nums)) != len(nums)
# print(containDuplicates([1, 2, 3, 1]))
def containDuplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# print(containDuplicates([1, 2, 3]))
def arrayIntersection(nums1,nums2):
    intersection = list(set(nums1) & set(nums2))
    return intersection
# print(arrayIntersection(nums1 = [1, 2, 2, 1], nums2 = [2, 2]))
def longestConsecutive(nums):
    if not nums:
        return 0
    maxLength = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            length = 1
            current_num = num
            while current_num + 1 in nums_set:
                length += 1
                current_num += 1
            maxLength = max(maxLength, length)
    return maxLength
# print(longestConsecutive([100, 4, 200, 1, 3, 2]))
# longest non-repeating substring
def longest_substr(s):
    n = len(s)
    left = 0
    char_set = set()
    max_substr = 0
    
    for right in range(n):
        # if char is repeated shrink the window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # otherwise
        char_set.add(s[right])
        max_substr = max(max_substr, right - left + 1)
    return max_substr
# print(longest_substr("abccabcbb"))
def max_subArray(nums):
    current_sum = 0
    max_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# print(max_subArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# two numbers that adds up to target
def twoSum(nums,target):
    num_to_index = {}
    
    for i,num in enumerate(nums):
        complement = target - num       
        if complement in num_to_index:
            return [num_to_index[complement],i]
        # add the num to hashmap
        num_to_index[num] = i
# print(twoSum([2, 7, 11, 15],9))
# product of array except self
def except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # left product
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    #right product
    right_product = 1
    for j in range(n - 1,-1,-1):
        result[j] = right_product
        right_product *= nums[j]
    return result
# print(except_self([1, 2, 3, 4]))
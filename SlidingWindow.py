def findMaxAverage2(nums,k):
    n = len(nums)
    current_sum = sum(nums[:k])
    max_avg = current_sum / k
    for i in range(k,n):
        current_sum += nums[i] - nums[i-k]
        max_avg = max(max_avg, current_sum / k)
    return max_avg
# print(findMaxAverage2([0,4,0,3,2],1))
def min_subArray_len(nums,t):
    window_start, min_len, current_sum,n = 0,float("inf"),0,len(nums)
    
    for window_end in range(n):
        current_sum += sum(nums[window_start:window_end])
        
        if current_sum >= t:
            min_len = min(min_len, window_end - window_start + 1)
            current_sum -= nums[window_start]
            window_start += 1
    return min_len if min_len != float("inf") else 0
# print(min_subArray_len([1,4,4],4))
def lengthOfLongestSubstring(s):
    left, str_length,n = 0,0,len(s)
    seen = set()
    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        str_length = max(str_length, right - left + 1)    
    return str_length
# print(lengthOfLongestSubstring("abcabcbb"))
def minSubArrayLen(target, nums):
    n,current_sum,left = len(nums),0,0
    min_len = float("inf")
    
    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right -left + 1)
            current_sum -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0
# print(minSubArrayLen(target = 11, nums = [1,2,3,4,5]))
def minSubArrayLen2(target, nums):
    n = len(nums)
    min_len = float("inf")
    left = 0
    current_sum = 0
    
    for right in range(n):
        current_sum += sum(nums[left:right])
        
        if current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0
from collections import defaultdict
def characterReplacement(s,k):
    left, longest_strSubstring, n, char_count, max_char_count = 0,float("-inf"),len(s), defaultdict(int),0
    
    for right in range(n):
        char_count[s[right]] += 1
        max_char_count = max(max_char_count, char_count[s[right]])
        while (right - left + 1) - max_char_count > k:
            char_count[s[left]] -= 1
            left += 1
        # longest_strSubstring = max(longest_strSubstring, right - left + 1)
    # return longest_strSubstring if longest_strSubstring != float("-inf") else 0
    return n - left
# print(characterReplacement(s = "ABAB", k = 2))
def maxTurbulenceSize(arr):
    n = len(arr)
    
    if n < 2:
        return n
    
    left = 0
    max_size = 1
    
    for right in range(1, n):
        # Check if the current segment is turbulent
        if right > 2 and \
           (arr[right] > arr[right - 1] and arr[right - 2] > arr[right - 1]) or \
           (arr[right] < arr[right - 1] and arr[right - 2] < arr[right - 1]):
            max_size = max(max_size, right - left + 1)
        elif arr[right] == arr[right - 1]:
            left = right
        else:
            left = right - 1
    max_size = max(max_size, n - left)
    return max_size
# print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
def longestNiceSubstring(s):
    n = len(s)
    left = 0
    output = ""
    for right in range(n - 1):
        if s[right].swapcase() not in s[right + 1:]:
            left = right + 1
        output = s[left:right]
    return output
# print(longestNiceSubstring("YazaAay"))
def arithmeticTriplets(nums, diff):
    num_set = set(nums)
    number_of_triplets = 0
    
    for num in nums:
        if num + diff in num_set and (num + 2 * diff in num_set):
            number_of_triplets += 1
    return number_of_triplets
# print(arithmeticTriplets([0, 1, 4, 6, 7, 10], diff = 3))
def longestNiceSubstring(s):
    n = len(s)
    nice_str = ""
    nice_substr_len = 0
    
    def isNice(subString):
        char_set = set(subString)
        for c in subString:
            if c.swapcase() not in char_set:
                return False
        return True
    
    for start in range(n):
        for end in range(start+ 1, n):
            subStr = s[start:end + 1]
            if isNice(subStr) and end - start + 1 > nice_substr_len:
                nice_substr_len = end - start + 1
                nice_str = subStr
    return nice_str
# print(longestNiceSubstring("YazaAay"))
def containsNearbyDuplicate(nums,k):
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1,n):
            if j - i <= k and nums[i] == nums[j]:
                return True
    return False
# print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
def containsNearbyDuplicate2(nums,k):
    n = len(nums)
    left = 0
    right = left + 1
    while left <= n - 2:
        if right > n - 1:
            left += 1
            right = left + 1
        if right - left <= k and nums[left] == nums[right]:
                return True
        right += 1
    return False
# print(containsNearbyDuplicate2([1,2,3,1,2,3],2))
def containsNearbyDuplicate3(nums, k):
    seen = {}
    for i,num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
# print(containsNearbyDuplicate3([1,2,3,1,2,3],2))
def findMaxAverage3(nums, k):
    n = len(nums)
    # i = 0
    max_avg = sum(nums[:k]) / k
    for j in range(1,n - k + 1):
        current_avg = sum(nums[j:k+j]) / k
        max_avg = max(max_avg, current_avg)
    return max_avg
# print(findMaxAverage3(nums = [5], k = 1))
def findMaxAverage4(nums,k):
    n = len(nums)
    current_sum = sum(nums[:k])
    max_avg = current_sum / k
    for i in range(k,n):
        current_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, current_sum / k)
    return max_avg
# print(findMaxAverage4(nums = [5], k = 1))
def findMaxAverage5(nums,k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    # [0,1,13,7,1,51,54]
    max_avg = float("-inf")
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
    for j in range(k,n+1):
        current_sum = prefix_sum[j] - prefix_sum[j - k]
        max_avg = max(max_avg, current_sum / k)
    return max_avg
# print(findMaxAverage5(nums = [1,12,-5,-6,50,3], k = 4))
# *******************
def minimumRecolors(blocks, k):
    n = len(blocks)
    min_operations = float("inf")
    
    for i in range(n-k+1):
        sub_block = blocks[i:k+i]
        print(sub_block)
        min_operations = min(min_operations, sub_block.count("W"))
    return min_operations
# print(minimumRecolors(blocks = "WBWBBBW", k = 2))
def intersect2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    p1, p2 = 0,0
    n = len(nums1)
    m = len(nums2)
    output = []
    while p1 < n and p2 < m:
        if nums1[p1] == nums2[p2]:
            output.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return output
# print(intersect2(nums1 = [1,1,2,2], nums2 = [2,2]))

def findAnagrams(s, p):
        p = sorted(p)
        n = len(s)
        i = 0
        j = i + len(p)
        output = []
        
        while j <= n:
            if sorted(s[i:j]) == p:
                output.append(i)
            j += 1
            i += 1
        return output
# print(findAnagrams("abab", "ab"))
from collections import Counter
def findAnagrams2(s,p):
    n = len(s)
    k = len(p)
    p_counter = Counter(p)
    s_counter = Counter()
    output = []
    
    for i in range(n):
        s_counter[s[i]] +=1
        
        if i >= k:
            if s_counter[s[i - k]] == 1:
                del s_counter[s[i - k]]
            else:
                s_counter[s[i - k]] -= 1
        if s_counter == p_counter:
            output.append(i - k + 1)
    return output
# print(findAnagrams2(s = "cbaebabacd", p = "abc"))
def longestSubarray(nums):
    n = len(nums)
    left = 0
    max_length = 0
    num_of_zeros = 0
    
    for right in range(n):
        if nums[right] == 0:
            num_of_zeros += 1
        while num_of_zeros > 1:
            if nums[left] == 0:
                num_of_zeros -= 1
            left += 1
        max_length = max(max_length, right - left)
    return max_length
# print(longestSubarray([0,1,1,1,0,1,1,0,1]))
def longestSubarray2(nums):
    n = len(nums)
    left = 0
    max_length = 0
    
    for right in range(1,n):
        while nums[left:right + 1].count(0) > 1:
            left += 1
        max_length = max(max_length, right - left)
    return max_length
# print(longestSubarray2([1,1,0,1]))
def dailyTemperatures(temperatures):
    n = len(temperatures)
    i = 0
    j = i + 1
    output = []
    
    while j < n:
        if temperatures[i] < temperatures[j]:
            output.append(j - i)
            i += 1
            j = i + 1
        elif j == n - 1:
            output.append(0)
            i += 1
            j = i + 1
        else:
            j += 1
        
    output.append(0)
    return output
# print(dailyTemperatures([30,60,90]))
def longestNiceSubstring5(s):
    n = len(s)
    long_substr = ""
    long_substr_len = 0
    
    def isNice(substring):
        char_set = set(substring)
        for c in substring:
            if c.swapcase() not in char_set:
                return False
        return True
    
    for left in range(n):
        for right in range(left + 1,n):
            substr = s[left:right + 1]
            # print(substr)
            if isNice(substr) and right - left + 1 > long_substr_len:
                print(substr)
                long_substr_len = right - left + 1
                long_substr = substr
    return long_substr
# print(longestNiceSubstring5("YazaAay"))
def longestNiceSubstring6(s):
    char_set = set(s)
    
    for i, char in enumerate(s):
        if char.swapcase() not in char_set:
            # recursively find nice string in left and right parts
            left = longestNiceSubstring6(s[:i])
            right = longestNiceSubstring6(s[i + 1:])
            return left if len(left) >= len(right) else right
    return s
print(longestNiceSubstring6("YazaAay"))
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
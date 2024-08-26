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


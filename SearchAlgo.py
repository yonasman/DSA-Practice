# search algorithm practices
#*********************
# LINEAR SEARCH
# ********************
def linear_search(nums,target):
    for num in nums:
        if target == num:
            return True
        else:
            return False
# print(linear_search([1,2,3,4,5],6))
# **********************
# BINARY SEARCH
#***********************
def binary_search(nums,target):
    n = len(nums)
    # initialize left and right pointers to track numbers window
    left = 0
    right = n - 1
    while right >= left:
        # initialize a mid pointer to check for the existence of the target
        mid = (left + right) // 2
        # return or update the pointers based on getting a target
        if nums[mid] == target:
            return True
        else:
            if target > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return False
# print(binary_search([1,2,3,4,5],7))
from bisect import bisect_left
def binary_search_with_bisect(nums,target):
    index = bisect_left(nums,target)
    if index < len(nums) and nums[index] == target:
        return True
    return False
# print(binary_search_with_bisect([1,3,4,5],2))
def binary_search_for_chars(s,target):
    n = len(s)
    left = 0
    right = n - 1
    while right >= left:
        mid = (left + right) // 2
        if s[mid] == target:
            return True
        else:
            if s[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return False
# print(binary_search_for_chars("abcdef",'r'))

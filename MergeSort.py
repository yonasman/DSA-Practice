# practicing merge sort
def merge(left, right):
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    # append the remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

def merge_sort(nums):
    n = len(nums)
    # if it contains at most one element return
    if n <= 1:
        return nums
    # middle index to split the array
    mid = n // 2
    # split the array in half
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    # return merged array
    return merge(left_half, right_half)

# print(merge_sort([1,5,2,9,8]))
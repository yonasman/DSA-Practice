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
# descending merge sort
def descending_merge(left, right):
    pass

def descend_merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    # split into 2 using middle index
    mid = n // 2
    left_half = descend_merge_sort(nums[:mid])
    right_half = descend_merge_sort(nums[mid:])
    # return the sorted and merged array
    return descending_merge(left_half, right_half)

def descending_merge(left_half, right_half):
    sorted_array = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    while i < len(left_half):
        sorted_array.append(left_half[i])
        i += 1
        
    while j < len(right_half):
        sorted_array.append(right_half[j])
        j += 1
    return sorted_array
print(descend_merge_sort([1,4,5,2,7,3]))
            
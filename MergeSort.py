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

# print(merge_sort([1, 20, 6, 4, 5]))
# descending merge sort
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
# print(descend_merge_sort([1,4,5,2,7,3]))
#merge a sorted array
def merger(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    mergedArray = []
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1
        # [1, 4, 7] and [2, 5, 6]
    # append the remaining elements
    # mergedArray.extend(arr1[i:])
    # mergedArray.extend(arr2[j:])
    # or
    while i < n:
        mergedArray.append(arr1[i])
        i += 1
    while j < n:
        mergedArray.append(arr2[j])
        j += 1
    return mergedArray
# print(merger([1,4,7],[2,5,6]))

# count number of inversions
def inversion_merge(left_half, right_half):
    sorted_arr = []
    i = j = 0
    inversion_count = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            inversion_count += len(left_half[i:])
            j += 1
    # append the remaining elements
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    
    return sorted_arr, inversion_count

def merge_sort_inversion(nums):
    n = len(nums)
    # if contains at most 1 element
    if n <= 1:
        return nums, 0
    mid = n // 2
    left,left_inversion_count = merge_sort_inversion(nums[:mid])
    right, right_inversion_count = merge_sort_inversion(nums[mid:])
    # merge and count split inversions
    merged, split_inversions = inversion_merge(left,right)
    
    total_inversions = left_inversion_count + right_inversion_count + split_inversions
    return merged, total_inversions
# print(merge_sort_inversion([1, 20, 6, 4, 5]))
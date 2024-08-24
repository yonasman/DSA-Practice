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
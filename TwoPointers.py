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
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
#[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# reversing an array without using two pointers
def reverse_arr2(nums):
    n = len(nums)
    reversed_arr = [0] * n
    for i in range(n):
        reversed_arr[i] = nums[n - 1 - i]
    return reversed_arr
# print(reverse_arr2([1,1,0,0]))
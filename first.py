import math

# practice python
# exercise 1
# *************************************



def date_slicer(date):
    year = date[0:4]
    month = date[5:7]
    day = date[8]
    return f"Year: {year} Month: {month} day:{day}"
# print(date_slicer("2020-23-4"))

# exercise 2
# **************************************
def reverse_string(str):
    str = str[-1::-1]
    return str
# print(reverse_string("hey"))

# exercise 3
# **************************************
def generate_right_triangle():
    for i in range(1,6):
        for j in range(0,1):
            print("* " * i)
# generate_right_triangle()

# exercise 4
# *************************************
# def GCF(num1,num2):
#     if(num1 > num2): 
#         n = num1
#     else: 
#         n = num2
#     max = 0
#     for i in range(1,n):
#         if(num1 % i == 0 and num2 % i == 0):
#             max = i
#     return max
# print(GCF(8,4))
# way 2
def GCF(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
# print(GCF(4,8))

# exercise 5
# *****************************************
def smallerNumbersThanCurrent(arr):
  output = []
  
  for n in arr:
    count = 0
    for m in arr:
      if(n > m):
         count += 1
    output.append(count)
  return output
# print(smallerNumbersThanCurrent([7,7,7,7]))
# lambda
area = lambda width, height:width * height
# print(area(3,4))

# exercise 6
# ***************************************
def solveQuadraticEquation(a,b,c):
    # calculating the discriminant
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        # two real solution
        x1 = (-b + (math.sqrt(discriminant))) / 2*a
        x2 = (-b - (math.sqrt(discriminant))) / 2*a
        return f"The two real solutions are {x1} and {x2}."
    elif discriminant == 0:
        # one real solution
        x = -b / 2*a
        return f"The only real solution is {x}"
    else:
        # Two complex solutions
        real_part = -b / 2*a
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"Two complex solutions {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"
# print(solveQuadraticEquation(1,5,4))
# exercise 8
# **************************************
# fibonacci
def fibonacci():
    first = 0
    second = 1
    i = 0
    print(first)
    print(second)
    while(i < 10):
        next = first + second
        first = second
        second = next
        i = i + 1
        print(next)
        
# fibonacci()
# print(0)
# print(1)
def rec_fibonacci(count, first_prev,sec_prev):
    if(count < 19):
        next = first_prev + sec_prev
        first_prev = sec_prev
        sec_prev = next
        print(next)
        count += 1
        rec_fibonacci(count,first_prev,sec_prev)
    else:
        return
# rec_fibonacci(2,0,1)
# linear search
def linear_search(arr,target):
    for item in arr:
        if(item == target):
            return True
    return False
# print(linear_search([1,2,3,4,5],0))
# bubble sort
def bubble_sort(arr):
    n = len(arr)
    # 5
    for i in range(n):
        # 0,1,2,3,4
        for j in range(n-i-1):
            # 4,3,2,1,0
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# print(bubble_sort([10,1,6,3,7]))
# timed bubble sort
from time import time
def timed_bubble_sort(arr):
    start = time()
    print(bubble_sort(arr))
    end = time()
    print(f"elapsed time {end - start} secs")
# timed_bubble_sort([1,3,2,9,5,6,7,4,4,7,9,1,2,3,4,5,5])
"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 

"""
# pseudo code
def common_prefix(strs):
    if not strs:
        return ""
    # set prefix to first string
    prefix = strs[0]
    for str in strs[1:]:
        while not str.startswith(prefix):
            # reduce the prefix by one last char
            prefix = prefix[:-1]
            # if prefix become empty return ""
            if not prefix:
                return ""
    return prefix
# print(common_prefix(["flower","flow","flight"]))
#  Remove Duplicates from Sorted Array
# def remove_duplicates(nums):
#     new_arr = []
#     # number of unique numbers
#     k = 0
#     for num in nums:
#         if num not in new_arr:
#             new_arr.append(num)
#             k += 1
#     return k
# print(remove_duplicates([1,1,2]))
def removeDuplicates(nums):
    if not nums:
        return 0
    # initialize the first pointer to track the place of unique elements
    k = 1
    for i in range(1,len(nums)):
        # 1,2
        if(nums[i] != nums[i - 1]):
            # place the current element in the k-th position
            nums[k] = nums[i]
            # increment unique elements count
            k += 1
    return k
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
"""Example 1: Two Sum II - Input Array Is Sorted
Problem: Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers."""
def two_sum(nums,target):
    # initialize the two pointers to start and end element
    left,right = 0,len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return f"index of the two elements is {left} and {right}"
        elif current_sum < target:
            left += 1
        else:
            right -= 1
# print(two_sum([6,2,3,4,5,6],7))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if(arr[j] > arr[j + 1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
# print(bubble_sort([1,2,3,4,5]))
# best case
def best_bubble_sort(arr):
    n = len(arr) - 1
    for j in range(n):
        if not swapped:
            break
        swapped = False
        for i in range(1,n - j):
            if(arr[i] > arr[i + 1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
    return arr
# print(bubble_sort([3,4,5,1,2]))
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i + 1,n):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i],arr[minIdx] = arr[minIdx],arr[i]
    return arr
# print(selection_sort([3,4,5,2,1,2]))
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# print(insertion_sort([5,3,1,4]))
# count sort
def count_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    count_range = max_val - min_val  + 1
    # initialize count array
    count_arr = [0] * count_range
    # count occurrence of each value
    for num in arr:
        count_arr[num- min_val] += 1
    # accumulate counts
    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    # output array
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1
    return output
# print(count_sort([2,1,3,4,4,5]))
"""
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
"""
def original_sentence(str):
    str = str.split(" ")
    n = len(str)
    for i in range(n - 1):
        # print(str[i])
        for j in range(n - i - 1):
            if(int(str[j][-1]) > int(str[j + 1][-1])):
                str[j],str[j+1] = str[j+1],str[j]
    str = [s[:-1] for s in str]
    return " ".join(str)
# print(original_sentence("is2 sentence4 This1 a3"))

def watermelon(w):
    if w % 2 == 0 and w >= 4:
        print("YES")
    else:
        print("NO")
def distinct(count, nums):
    k = 1
    for i in range(1,len(nums)):
         if(nums[i] != nums[i - 1]):
             nums[k] = nums[i]
             k += 1
    return k
    
# print(distinct(5,
def sum_two(arr, result):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if(arr[i] + arr[j] == result):
                return f"{i} and {j}"
# print(sum_two([2,7,5,1],8))
# Widest Vertical Area Between Two Points Containing No Points
# pseudo code
# sort

# answer

def widest_vertical_area(points):
    n = len(points) - 1
    for i in range(n):
        for j in range(n - i):
            if(points[j][0] > points[j+1][0]):
                points[j], points[j+1] = points[j+1], points[j]
    widest_area = 0           
    for i in range(n - 1):
        if(points[i + 1][0] - points[i][0] > widest_area):
            widest_area = points[i + 1][0] - points[i][0]
    return widest_area
# print(widest_vertical_area([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
"""
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.

Example 1:

Input: nums = [5,4,2,3]
[2,3,4,5]
Output: [3,2,5,4]
"""
def number_game(nums):
    nums.sort()
    n = len(nums)
    new_arr = []
    # 0,1
    for i in range(0,n,2):
        if i + 1 < n:
            A = nums[i]
            B = nums[i+1]
            new_arr.append(B)
            new_arr.append(A)
    return new_arr
# print(number_game([5,4,2,3]))
"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
"""
# pseudo code
# 1- define a func named find_target_index that takes arr as a param
# iterate and find the index of target element
# return a list of index
def find_target_index(nums,target):
    n = len(nums)
    nums.sort()
    new_arr = []
    for i in range(n):
        if(nums[i] == target):
            new_arr.append(i)
    return new_arr
# print(find_target_index([1,2,5,2,3],5))
"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

"""
# pseudo code
# define a func named findContentChildren that takes two list params
# 
def findContentChildren(g,s):
    g.sort()
    s.sort()
    content,i,j = 0,0,0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            content += 1
            i += 1
        j += 1
    return content
# print(findContentChildren([1,2,3],[]))

# *************
# merge two sorted arrays
arr1,arr2 = [1,2,3,4,7], [2,3,4,5,6]
# brute force approach
def merger(arr1,arr2):
    merged = []
    for i in range(len(arr1)):
        merged.append(arr1[i])
    for j in range(len(arr2)):
        merged.append(arr2[j])
    merged.sort()
    return merged
# print(merger(arr1, arr2))

# using two pointers
def array_merged(arr1, arr2):
    i,j = 0,0
    merged_arr = []
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    # if there are any remaining elements
    while(i < len(arr1)):
        merged_arr.append(arr1[i])
        i += 1
    while(j < len(arr2)):
        merged_arr.arr2[j]
        j += 1
    return merged_arr
print(array_merged([1,2,3,4,7], [2,3,4,5,6]))
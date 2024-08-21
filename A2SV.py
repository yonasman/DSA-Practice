# problem 1
# ************************
"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
def reverseString(s):
    s = "".join(s)
    s = s[::-1]
    s = list(s)
    print(s)
# reverseString( ["H","a","n","n","a","h"])
def reverseString2(s):
    n = len(s)
    p1 = 0
    p2 = n -1
    
    while p1 < p2 :
        s[p1],s[p2] = s[p2],s[p1]
        p1 += 1
        p2 -= 1
    print(s)
# print(reverseString2(["H","a","n","n","a","h"]))
# problem 2
"""
1768. Merge Strings Alternately
Easy

3904

98

Add to List

Share
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
def mergeAlternately(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    mergedString = ""
    for i in range(min(n1,n2)):
        mergedString += word1[i]
        mergedString += word2[i]
    if(n2 > n1):
            mergedString += word2[n1:]
    elif n1 > n2:
            mergedString += word1[n2:]
    return mergedString
# print(mergeAlternately(word1 = "abc", word2 = "pqrzx"))
def merge(nums1, m, nums2,n):
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    print(nums1)
# merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [4,5,6], n = 3)
"""
problem 4
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
def moveZeroes(nums):
    non_zero_idx = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[i],nums[non_zero_idx] = nums[non_zero_idx],nums[i]
            non_zero_idx += 1
    print(nums)
# moveZeroes([0,1,0,3,12])
def moveZeros2(nums):
    n = len(nums)
    non_zero_idx = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_idx] = nums[i]
            non_zero_idx += 1
    for i in range(non_zero_idx,n):
        nums[i] = 0
    # print(nums)
# moveZeros2([0,1,0,3,12])
# problem 5
"""
1365. How Many Numbers Are Smaller Than the Current Number
Easy
Add to List

Share
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
def smallerNumbersThanCurrent(nums):
    n = len(nums)
    output = []
    # sortedNums = sorted(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] > nums[j]:
                count += 1
        output.append(count)
    return output
# print(smallerNumbersThanCurrent([8,1,2,2,3]))
[1,2,2,3,8]
def smallerNumbersThanCurrent2(nums):
    sortedNums = sorted(nums)
    n = len(nums)
    output = []
    for i in range(n):
        print(sortedNums[:nums[i]])
        output.append(len(sortedNums[:sortedNums.index(nums[i])]))
    return output
# print(smallerNumbersThanCurrent2([8,1,2,2,3]))
def smallerNumbersThanCurrent3(nums):
    sortedNums = sorted(nums)
    # create a dict to count the numbers smaller than current
    smaller_count = {}
    for i, num in enumerate(sortedNums):
        if num not in smaller_count:
            smaller_count[num] = i
    result = [smaller_count[num] for num in nums]
    return result
# print(smallerNumbersThanCurrent3([8,1,2,2,3]))
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
def majorityElement(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return max(d,key = d.get)
# print(majorityElement([3,3,4]))
"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
"""
def calPoints(ope):
    result = []
    for op in ope:
        if op == "C":
            result.pop()
        elif op == "D":
            result.append(result[-1] * 2)
        elif op == "+":
            result.append(result[-1] + result[-2])
        else:
            result.append(int(op))
    return sum(result)
# print(calPoints(["5","2","C","D","+"]))
def repeatedCharacter(s):
    n = len(s)
    idx = float("inf")
    for i in range(n):
        for j in range(i + 1,n):
            if s[i] == s[j]:
                idx = min(idx, j)
    print(s[idx])
# repeatedCharacter("abcdd")
def repeatedCharacter2(s):
    seen = set()
    for letter in s:
        if letter in seen:
            return letter
        else:
            seen.add(letter)
# print(repeatedCharacter2("abccbaacz"))
def repeatedCharacter3(s):
    seen = {}
    for letter in s:
        if letter in seen:
            return letter
        seen[letter] = 1
# print(repeatedCharacter3("abccbaacz"))
# ***************************************
# 4 = number of applicant, 3 apartment, 5 difference
# 1- 60
# 2- 45 
# 3- 80
# 4- 60
# 30 60 75

def apartment(p,a,d,apart,size):
    n = p
    m = a
    i = 0
    j = 0
    assign = 0
    
    while i < n and j < m:
        apart.sort()
        size.sort()
        
        if size[i] >= apart[j] - d and size[i] <= apart[j] + d:
            assign += 1
            i += 1
            j += 1
        elif size[i] < apart[j] - d:
            i += 1
        else:
            j += 1
    return assign
# print(apartment(4,3,5,[30,60,75],[60,45,80,60]))
# n = input() 
# nums = list(map(int,input().split()))
def targetSum(n,nums):
    max_sum = global_sum = nums[0]
    
    for i in range(1,n):
        max_sum = max(nums[i], max_sum + nums[i])
        if max_sum > global_sum:
            global_sum = max_sum
    return global_sum
# print(targetSum(8,[-1, 3, -2, 5, 3, -5, 2, 2]))
def countSubArray(n, t, nums):
    p1 = 0
    count = 0
    current_sum = 0

    for p2 in range(n):
        current_sum += nums[p2]

        # While the current_sum is greater than t, shrink the window
        while current_sum > t and p1 <= p2:
            current_sum -= nums[p1]
            p1 += 1

        # Check if the current_sum equals t
        if current_sum == t:
            count += 1
    return count

# Example usage
# print(countSubArray(5, 7, [2, -1, 3, 5, -2])) 


def smallerCount(n,nums):
    output = []
    for i in range(n):
        nearest_idx = -1
        for j in range(i):
            if nums[j] < nums[i]:
                nearest_idx = j
        output.append(nearest_idx)
    print(output)
# smallerCount(8,[2, 5, 1, 4, 8, 3, 2, 5])
# def leftRightDifference(nums):
#     n = len(nums)
#     output = []
#     for i in range(n):
#         if i == 0:
#             output.append(0)
#         else:
#             #[10,4,8,3] [0,10,14,22]
#             output.append(output[i - 1] + nums[i - 1])
#     return output
# print(leftRightDifference([10,4,8,3]))
def GCF(num1, num2):
    if num1 > num2:
        min_num = num2
    else:
        min_num = num1
    gcf = 0
    for i in range(2,min_num):
        if num1 % i == 0 and num2 % i == 0:
            gcf = max(gcf, i)
    return gcf
# print(GCF(48,180))
def GCF2(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1
# print(GCF2(48,180))
# ********************************
# SORTING ALGORITHM
# ********************************
# bubble sort
# ***********
def bubbleSort(nums):
    n = len(nums)
    swap = False
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swap = True
    if not swap:
        print("already sorted!")
        return nums
    return nums
# print(bubbleSort([1,2,3,4,5]))

def sortPeople(names, heights):
    n = len(heights)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if heights[j] < heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
                swap = True
        if not swap:
            break
    return names
# print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))

# selection sort
# **********************************
# pseudo code
def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1,n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
# print(selectionSort([5,2,6,2,1,1]))
#[2,5,6,2,1,1]
# insertion sort
def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
# print(insertionSort([5,2,6,2,1,1]))
def countingSort(nums):
    n = len(nums)
    count = [0] * (max(nums) + 1)
    
    for num in nums:
        count[num] += 1
    for i in range(1,n+1):
        count[i] += count[i - 1]
    print(count)
    output = [0] * n
    i = n - 1
    while i >= 0:
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
        i -= 1
    return output
# print(countingSort([1,4,1,2,7,5,2]))
def sortPeople2(names, heights):
    n = len(heights)
    max_h = max(heights)
    count = [0] * (max_h + 1)
    for h in heights:
        count[h] += 1
    for i in range(1, max_h + 1):
        count[i] += count[i - 1]
    outputHeights = [0] * n
    outputNames = [0] * n
    for i in range(n - 1, -1, -1):
        height = heights[i]
        name = names[i]
        
        position = count[height] - 1
        outputHeights[position] = height
        outputNames[position] = name
        
        # decrease the count for height
        count[height] -= 1
    return outputNames
# print(sortPeople2(names = ["Mary","John","Emma"], heights = [180,165,170]))
    
        
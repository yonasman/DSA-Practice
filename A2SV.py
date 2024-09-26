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
def numberGame(nums):
    output = []
    nums.sort()
    n = len(nums)
    
    for i in range(0,n,2):
        if i + 1 < n:
            a = nums[i]
            b = nums[i + 1]
            output.append(b)
            output.append(a)
    return output
# print(numberGame([5,4,2,3]))
def maxWidthOfVerticalArea(points):
    points.sort()
    widest_vert_area = 0
    n = len(points)
    for i in range(n - 1):
        current_vert_area = points[i + 1][0] - points[i][0]
        widest_vert_area = max(widest_vert_area, current_vert_area)
#     return widest_vert_area
# print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
def sortSentence(sent):
    splittedSent = sent.split()
    n = len(splittedSent)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if splittedSent[min_idx][-1] > splittedSent[j][-1]:
                min_idx = j
        splittedSent[i], splittedSent[min_idx] = splittedSent[min_idx], splittedSent[i]
    splittedSent = [s[:-1] for s in splittedSent]    
    output = " ".join(splittedSent)
    return output
# print(sortSentence("is2 sentence4 This1 a3"))
def findContentChildren(g,s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    contented_children = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            contented_children += 1
            i += 1
        j += 1
    return contented_children
# print(findContentChildren([10,9,8,7], [5,6,7,8]))
def merge(nums1,m,nums2,n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
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
        p -= 1
        p2 -= 1
    return nums1
# print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
def sortVowels(s):
    v = "EOUAIeaoui"
    n = len(s)
    vowels = []
    for i in range(n):
        if s[i] in v:
            vowels.append(s[i])
    vowels.sort()
    s = list(s)
    vowel_idx = 0
    for i in range(n):
        if s[i] in v:
            s[i] = vowels[vowel_idx]
            vowel_idx += 1
    return "".join(s)
# print(sortVowels("lEetcOde"))
def numIdenticalPairs(nums):
        freq = {}
        count = 0
        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return count
# print(numIdenticalPairs([1,2,3,1,1,3]))
def isAnagram(s1,s2):
    d1 = {}
    d2 = {}
    for s in s1:
        if s in d1:
            d1[s] += 1
        else:
            d1[s] = 1
    for s in s2:
        if s in d2:
            d2[s] += 1
        else:
            d2[s] = 1
    # for key in d1.keys():
    #     if key not in d2.keys() or d1[key] != d2[key]:
    #         return False
    
    return d1 == d2
# print(isAnagram(s1="bbcc", s2="ccbc"))
def di(s):
    s1 = {}
    for i in range(len(s)):
        s1[s[i]] = 1 + s1.get(s[i],0)
    return s1
# print(di("bbcc"))
def isPalindrome(s):
    let = "abcdefghijklmnopqrstuvwxyz1234567890"
    letters = ""
    s = s.lower()
    for l in s:
        if l in let:
            letters += l
    return letters == letters[::-1]
# print(isPalindrome("OP"))
def isPalindrome2(s):
    s = s.lower()
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    newLet = ""
    for l in s:
        if l in letters:
            newLet += l
    
    p1 = 0
    p2 = len(newLet) - 1
            
    while p1 <= p2: 
        if newLet[p1] != newLet[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
# print(isPalindrome2("aba"))
def intersect(nums1, nums2):
    output = []
    nums1.sort()
    nums2.sort()
    p1,p2 = 0,0
    
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            output.append(nums1[p1])
            p2 += 1
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return output
# print(intersect([4,9,5],[9,4,9,8,4]))
# print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
def maxIceCream(costs, coins):
    n = len(costs)
    
    count_arr = [0] * (max(costs) + 1)
    
    for cost in costs:
        count_arr[cost] += 1
    # print(count_arr)
    for i in range(1,max(costs) + 1):
        count_arr[i] += count_arr[i - 1]
    sortedCosts = [0] * n
    for i in range(n - 1,-1,-1):
        cost = costs[i]
        position = count_arr[cost] - 1
        sortedCosts[position] = cost
        count_arr[cost] -= 1
    
    num_of_ice_cream = 0
    current_cost = 0
    for cost in sortedCosts:
        if current_cost + cost <= coins:
            current_cost += cost
            num_of_ice_cream += 1
            print(current_cost)
    return num_of_ice_cream
# print(maxIceCream([10,6,8,7,7,8],5))
def maxIceCream2(costs, coins) :
    num_of_ice_creams = 0
    costs.sort()
    for c in costs:
        if c <= coins:
            num_of_ice_creams += 1
            coins -= c
    return num_of_ice_creams
# print(maxIceCream([10,6,8,7,7,8],5))
# ****************************
import math
def distance_from_origin(points):
    return math.sqrt(points[0] ** 2 + points[1] ** 2)
# print(distance_from_origin([3,4]))
def kClosest(points,k):
    sortedPoints = sorted(points, key=distance_from_origin)
    # print(sortedPoints)
    return sortedPoints[:k]
# print(kClosest( points = [[3,3],[5,-1],[-2,4]], k = 2))
def kClosest(points,k):
    distances = [(point, point[0] ** 2 + point[1]**2) for point in points]
    distances.sort(key=lambda x:x[1])
    return [point for point, distance in distances[:k]]
# print(kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
# a2sv problems
from collections import Counter
def findLHS(nums):
    maxHarmoniousLen = 0
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num,0) + 1
    for num in nums:
        if num + 1 in hashMap:
            maxHarmoniousLen = max(maxHarmoniousLen, hashMap[num] + hashMap[num + 1])
    return maxHarmoniousLen
# print(findLHS([1,3,2,2,5,2,3,7]))
def leftRightDifference(nums):
    n = len(nums)
    leftSum = [0] * n
    rightSum = [0] * n
    output = []
    for i in range(1,n):
        leftSum[i] = leftSum[i - 1] + nums[i-1]
    for j in range(n - 2,-1,-1):
        rightSum[j] = rightSum[j + 1] + nums[j + 1] 
    for k in range(n):
        output.append(abs(leftSum[k] - rightSum[k]))
    return output
# print(leftRightDifference([1]))
def leftRightDifference(nums):
    n = len(nums)
    leftSum = 0
    totalSum = sum(nums)
    output = []
    for i in range(n):
        rightSum = totalSum - leftSum - nums[i]
        output.append(abs(leftSum - rightSum))
        leftSum += nums[i]
    return output
# print(leftRightDifference([10,4,8,3]))
def productExceptSelf(nums):
    totalProduct = math.prod(nums)
    output = []
    for num in nums:
        output.append(int(totalProduct / num) )
    return output
# print(productExceptSelf([1,2,3,4]))
def productExceptSelf2(nums):
    output = []
    for i in range(len(nums)):
        prefixProd = math.prod(nums[:i])
        suffixProd = math.prod(nums[i+1:])
        output.append(prefixProd * suffixProd)
    return output
# print(productExceptSelf2([-1,1,0,-3,3]))
def productExceptSelf3(nums):
    n = len(nums)
    output = [1] * n
    # prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    # suffix products
    suffix = 1
    for j in range(n - 1,-1,-1):
        output[j] *= suffix
        suffix *= nums[j]
    return output
# print(productExceptSelf3([-1,1,0,-3,3]))
def pivotArray(nums, pivot):
    # lists to store respective elements
    less = []
    equal = []
    greater = []
    for num in nums:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return less + equal + greater
# print(pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))
def pivotArray2(nums, pivot):
    n = len(nums)
    output = [0] * n
    left = 0
    # build the left elements
    for num in nums:
        if num < pivot:
            output[left] = num
            left += 1
    # build the equal
    right = left
    for num in nums:
        if num == pivot:
            output[right] = num
            right += 1
    # build the greater elements
    for num in nums:
        if num > pivot:
            output[right] = num
            right += 1
    return output
# print(pivotArray2([9,12,5,10,14,3,10], 10))
def maxArea(nums):
    n = len(nums)
    max_area = 0
    left = 0
    right = n - 1
    while left < right:
        current_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(current_area, max_area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_area
# print(maxArea([1,1]))
def minSteps(s,t):
    hashMapS = {}
    hashMapT = {}
    minSteps = 0
    for c in s:
        hashMapS[c] = hashMapS.get(c,0) + 1
    for c in t:
        hashMapT[c] = hashMapT.get(c,0) + 1
        
    for key in hashMapS:
        if key in hashMapT:
            minSteps += max(0, hashMapS[key] - hashMapT[key])
        else:
            minSteps += hashMapS[key]
    return minSteps
# print(minSteps( s = "leetcode", t = "practice"))
def corpFlightBookings(bookings,n):
    answer = [0] * (n + 1)
    for first,last,seats in bookings:
        answer[first - 1] += seats
        answer[last] -= seats
    print(answer)
    for i in range(1,len(answer)):
        answer[i] += answer[i - 1]
    return answer[:n]
# print(corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))
def corpFlightBookings2(bookings, n):
    answer = [0] * (n + 1)
    for first,last,seats in bookings:
        for i in range(first,last + 1):
            answer[i - 1] += seats
    return answer[:n]
# print(corpFlightBookings2([[1,2,10],[2,3,20],[2,5,25]],5))
def numOfPairs(nums,target):
    num_of_pairs = 0
    n = len(nums)
    for i in range(n):
        num = nums[i]
        if target.startswith(num):
            remaining = target[len(num):]
            for j in range(n):
                if i != j and remaining == nums[j]:
                    num_of_pairs += 1
    return num_of_pairs
# print(numOfPairs(nums = ["1","1","1"], target = "11"))
def maxProfit(prices):
    if not prices:
        return 0
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit
# print(maxProfit([7,6,4,3,1]))
#A2SV question-1
# ***************
#Convert the Temperature
def convertTemperature2(celsius):
    kelvin = 273.15 + celsius
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
# print(convertTemperature2(celsius = 36.50))
# Fizz Buzz
#***************************
def fizzBuzz(n):
    output = []
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(f'{i}')
    return output
# print(fizzBuzz(3))
def smallestEvenMultiple(n):
    if n % 2 == 0:
        return n
    else:
        return n *2
# print(smallestEvenMultiple(6))
# number of good pairs
def numIdenticalPairs(nums):
    n = len(nums)
    numOfPairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                numOfPairs += 1
    return numOfPairs
# print(numIdenticalPairs([1,2,3,1,1,3]))
# using hashmap
def numIdenticalPairs2(nums):
    [1,2,3]
    numOfPairs = 0
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num,0) + 1
    for value in hashMap.values():
        if value > 1:
            numOfPairs += (value * (value - 1)) // 2
    return numOfPairs
# print(numIdenticalPairs2([1,1,1,1]))
# way3
def numIdenticalPairs3(nums):
    hashMap = {}
    numOfPairs = 0
    for num in nums:
        if num in hashMap:
            numOfPairs += hashMap[num]
            hashMap[num] += 1
        else:
            hashMap[num] = 1
    return numOfPairs
# print(numIdenticalPairs3([1,1,1,1]))
# practice sorting algorithm
# problem 1
# Problem: Sort an Array of Student Scores
def bubble_sort_student_scores(scores:list) -> list:
    n = len(scores)
    # handle edge cases
    if(n <= 1):
        return scores
    # algorithm implementation
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if scores[j] > scores[j+1]:
                scores[j],scores[j+1] = scores[j+1],scores[j]
                swapped = True
        if(not swapped):
            break
    return scores
# print(bubble_sort_student_scores([88, 95, 70, 100, 92, 85, 78, 84, 65, 78]))
# problem 2
# sort people based on height
def sortPeople(names,heights):
        n = len(names)
        
        for i in range(n - 1):
            for j in range(n - i - 1):
                if(heights[j] < heights[j+1]):
                    names[j],names[j+1] = names[j+1],names[j]
                    heights[j],heights[j+1] = heights[j+1],heights[j]
        return names
# print(sortPeople(["Alice","Bob","Bob"],
# [155,185,150]))
# *******************************
# problem 3
# Problem: Sort an Array of Objects by a Key
# students = [
#   {"name": "Alice", "score": 88},
#   {"name": "Bob", "score": 95},
#   {"name": "Charlie", "score": 70},
#   {"name": "David", "score": 100},
#   {"name": "Eve", "score": 92}
# ]
def bubble_sort_students(students:list) -> list:
    n = len(students) 
    # handle edge case
    if(n < 2):
        return students
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if students[j]["score"] > students[i]["score"]:
                students[j]["score"],students[j+1]["score"] = students[j+1]["score"],students[j]["score"]
                swapped = True
        if(not swapped):
            return students
    return students
s = [{"name": "Eve", "score": 92}]
# print(bubble_sort_students(s))
# selection sort

a = [3,2,5,1,4,7]
def minimum(nums):
    n = len(nums)
    # 0,1,2
    for i in range(n):
        min_idx = i
        swapped = False
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                swapped = True
                min_idx = j
        if(not swapped):
            break
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
        
    return nums
# print(minimum(a))
# problem 4
# sort strings using selection sort
def sortStrings(strings):
    n = len(strings)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(strings[j] < strings[min_index]):
                min_index = j
        strings[i],strings[min_index] = strings[min_index],strings[i]
    return strings
# print(sortStrings(["banana", "apple", "cherry", "date"]))
# problem 5
# sort people by age
def sortPeople(peoples):
    n = len(peoples)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if(peoples[j]["age"] < peoples[min_idx]["age"]):
                min_idx = j
        peoples[i],peoples[min_idx] = peoples[min_idx],peoples[i]
    return peoples
# print(sortPeople([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]))
# problem 6
# Sorting with Duplicates
def sortDuplicates(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums
# print(sortDuplicates([5, 1, 3, 5, 2, 1]))
def sum_upto_middle(nums):
    n = len(nums)
    mid = n // 2 + 1
    prefix = [0] * mid
    prefix[0] = nums[0]
    for i in range(1,mid ):
        prefix[i] = prefix[i - 1] + nums[i]
    return prefix
# print(sum_upto_middle([1,2,3,4,5]))
# counting sort
def countingSort(nums):
    n = len(nums)
    min_num = min(nums)
    max_num = max(nums) 
    idx_range =  max_num - min_num + 1
    count_array = [0] * idx_range
    output = [0] * idx_range
    
    for num in nums:
        count_array[num - min_num] += 1

    for i in range(1,n):
        count_array[i] += count_array[i - 1]
    
    for num in nums:
        count_array[num - min_num] -= 1
        output[count_array[num - min_num]] = num
    return output
# print(countingSort([1,4,1,2,7,5,2]))

# leet code
def sortPeople(names, heights):
        n = len(heights)
        max_hgt = max(heights)
        count_arr = [0] * (max_hgt + 1)
        
        for h in heights:
            count_arr[h] += 1
            
        for i in range(1,max_hgt + 1):
            count_arr[i] += count_arr[i - 1]
        
        output_names = [0] * n
        output_heights = [0] * n
        
        i = n - 1
        
        while(i >= 0):
            h = heights[i]
            pos = count_arr[h] - 1
            output_heights[pos] = h
            output_names[pos] = names[i]
            count_arr[h] -= 1
            i -= 1
        output_names.reverse()
        return output_names
# print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# names = ["Mary","John","Emma"], heights = [180,165,170]
def cS(nums):
    n = len(nums)
    max_num = max(nums)
    count = [0] * (max_num + 1)
    
    for num in nums:
        count[num] += 1
    
    for i in range(1,max_num + 1):
        count[i] += count[i - 1]
    
    output = [0] * n
    i = n - 1
    # 6
    while(i >= 0):
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
        i -= 1
    return output
# print(cS([180,165,170]))
# ***********************
# prefix sum
# ***********************
"""1. Calculate the Sum:
 - Calculate the sum of the elements between the first and middle index for
the following array:
 `nums = [1, 13, 14, 76, 89, 100, 34]`"""
def sumUpToMiddle(nums):
    n = len(nums)
    mid = n // 2 + 1
    sum = 0
    for i in range(mid):
        sum += nums[i]
    return sum
# print(sumUpToMiddle([1,2,3]))
class NumArray:
    def sumToMid(self,nums):
        n = len(nums)
        mid = n // 2 + 1
        sum = 0
        for i in range(mid):
            sum += nums[i]
        return sum
n = NumArray()
# print(n.sumToMid([1,2,3]))
"""1637. Widest Vertical Area Between Two Points Containing No Points
Easy

932

1722

Add to List

Share
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area."""
def maxWidthOfVerticalArea(points):
        n = len(points)
        # sort the array
        points.sort()
        #  calculating the max vertical width
        widest_vert_area = 0
        for i in range(n - 1):
            current_width = points[i + 1][0] - points[i][0]
            widest_vert_area = max(widest_vert_area,current_width)
        return widest_vert_area 
# print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))

"""
2974. Minimum Number Game
Easy

223

16

Add to List

Share
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.
"""
def numberGame(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if(nums[j] < nums[min_idx]):
                nums[min_idx],nums[j] = nums[j], nums[min_idx]
    output = []
    for i in range(0,n,2):
        if i + 1 < n:
            a = nums[i]
            b = nums[i + 1]
            output.append(b)
            output.append(a)
    return output
# print(numberGame([2,5]))
"""
1859. Sorting the Sentence
Easy

2189

78

Add to List

Share
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""
def sortSentence(sent):
    word_list = sent.split(" ")
    n = len(word_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if int(word_list[j][-1]) < int(word_list[min_idx][-1]):
                word_list[j],word_list[min_idx] = word_list[min_idx],word_list[j]
    cleaned_words = [word[:-1] for word in word_list]
    return " ".join(cleaned_words)
# print(sortSentence("is2 sentence4 This1 a3"))
"""
2089. Find Target Indices After Sorting Array
Easy

1790

92

Add to List

Share
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""
# def targetIndices(nums):
#     n = len(nums)
#     min_val = min(nums)
#     max_val = max(nums)
#     range_val =  max_val - min_val + 1
#     count = [0] * (range_val)
    
#     for n in nums:
#         count[n - min_val] += 1
#     for i in range(1,range_val):
#         count[i] += count[i - 1]
    
#     output = [0] * n
#     for j in range(n):
#         index = count[nums[j] - min_val] - 1
#         output[index] = nums[j]
#         count[nums[j] -  min_val] -= 1
#     return output
def targetIndices(nums,target):
    n = len(nums)
    min_val = min(nums)
    max_val = max(nums)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    
    # Count the occurrences of each number
    for num in nums:  
        count[num - min_val] += 1
    
    # Update the count array to store the cumulative counts
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    sorted_arr = [0] * n
    
    # Place the elements in sorted order
    for j in range(n):
        index = count[nums[j] - min_val] - 1  # Subtract 1 for zero-based index
        sorted_arr[index] = nums[j]
        count[nums[j] - min_val] -= 1
    output = []
    for i in range(n):
        if sorted_arr[i] == target:
            output.append(i)
    return output
# print(targetIndices(nums = [1,2,5,2,3], target = 3))  # Expected Output: [1, 2, 3, 4]
"""
455. Assign Cookies
Easy

3945

374

Add to List

Share
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""
def findContentChildren(g,s):
    g.sort()
    s.sort()
    contented_children,i,j = 0,0,0
    while(i < len(g) and j < len(s)):
        if s[j] >= g[i]:
            contented_children += 1
            i += 1
        j += 1
    return contented_children
# print(findContentChildren(g = [1,2,3], s = [3]))
def merge(num1,m,num2,n):
    p1,p2 = m - 1,n - 1
    p = n + m
    while(p1 >= 0 and p2 >= 0):
        if num1[p1] < num2[p2]:
            num1[p] = num1[p1]
            p1 -= 1
        else:
            num1[p] = num1[p2]
            p2 -= 1
        p -= 1
    while(p2 >= 0):
        num1[p] = num1[p2]
        p2 -= 1
        p -= 1
    return num1
# print(merge(num1 = [1], m = 1, num2 = [], n = 0))
# sort vowels
def sortVowels(s):
        s = list(s)
        n = len(s)
        v = "aeuioAOUIE"
        for i in range(n):
            if(s[i] in v or s[i].upper() in v):
                print(s[i])
                for j in range(i,n):
                    if(s[j] in v or s[j].upper() in v):
                        if(s[i] > s[j]):
                            s[i],s[j] = s[j],s[i]
        return "".join(s)
# print(sortVowels("SrSuArHDvA"))
def sortVowel(string):
    n = len(string)
    v = "aeuioAOUIE"
    vowels = []
    for s in string:
        if s in v:
            vowels.append(s)
    vowels.sort()
    s = list(string)
    vowel_idx = 0
    for i in range(len(s)):
        if s[i] in v:
            s[i] = vowels[vowel_idx]
            vowel_idx += 1
    return "".join(s)
# print(sortVowel("SrSuArHDvA"))
def pivotIndex( nums):
        n = len(nums)
        for p1 in  range(n):
            sum_to_p1 = sum(nums[:p1])
            for p2 in range(p1,n):
                if sum_to_p1 == sum(nums[p1+ 1:n]):
                    return p1
                else:
                    p2 += 1
            p1 +=1
        return -1
# print(pivotIndex([1,2,3]))
# *********************************
# TWO POINTERS PRACTICE
# *********************************
# brute force for merging array
def merger(nums1,nums2):
    newArr = []
    for i in range(len(nums1)):
        newArr.append(nums1[i])
    for j in range(len(nums2)):
        newArr.append(nums2[j])
    newArr.sort()
    return newArr
# print(merger([1,2,3,4],[2,2,3]))
def pointerMerger(nums1,nums2):
    mergedArray = []
    p1,p2 = 0,0 
    while(p1 < len(nums1) and p2 < len(nums2)):
        if nums1[p1] <= nums2[p2]:
            mergedArray.append(nums1[p1])
            p1 += 1
        else:
            mergedArray.append(nums2[p2])
            p2 += 1
    # handling the remaining elements
    while(p1 < len(nums1)):
        mergedArray.append(nums1[p1])
        p1 += 1
    while(p2 < len(nums2)):
        mergedArray.append(nums2[p2])
        p2 += 1
    return mergedArray
# print(pointerMerger([1,2,3,4],[2,2,3]))
def mergeArr(nums1,m,nums2,n):
    p1,p2 = m - 1,n - 1
    p = m + n - 1
    while(p1 >= 0 and p2 >= 0):
        if(nums1[p1] > nums2[p2]):
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    # handling the remaining elements
    while(p2 >= 0):
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    return nums1
# print(mergeArr(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

def merge_arrays(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    # p1,p2,p = n - 1,m - 1, m + n -1
    p1,p2 = 0,0
    # output
    output = []
    while p1 < n and p2 < m:
        if nums1[p1] < nums2[p2]:
            output.append(nums1[p1])
            p1 += 1
        else:
            output.append(nums2[p2])
            p2 += 1
        p += 1
    while(p2 < m):
        output.append(nums2[p2])
        p2 += 1
    return output
# print(merge_arrays(nums1 = [1,2,3], nums2 = [2,5,6]))

# Problem: Given a sorted array of integers, find two numbers that add up to a given target.

def target_sum(nums,target):
    # p1,p2 = 0,p1 + 1
    n = len(nums)
    # output
    output = []
    for p1 in range(n):
        for p2 in range(p1 + 1,n):
            if nums[p1] + nums[p2] == target:
                output.append(nums[p1])
                output.append(nums[p2])
    return output
# print(target_sum([1,2,3,4,5],0))
def find_target_pairs(nums,target):
    n = len(nums)
    left,right = 0,n - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return([nums[left],nums[right] ])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
# print(find_target_pairs([1,2,3,4,5],6))

# Problem: Given a sorted array, remove the duplicates in place and return the new length of the array.
# [1,2,3,3,4]
def removeDuplicates(nums):
    n = len(nums)
    if not nums:
        return 0
    p1 = 0
    for p2 in range(1,n):
        if nums[p1] != nums[p2]:
            p1 += 1
            nums[p1] = nums[p2]
            
    return len(nums[:p1 + 1])
# print(removeDuplicates([1,2,3,3,4]))
def flipAndInvertImage(image):
    for img in image:
        p1 = 0
        p2 = len(img) - 1
        while(p1 <= p2): 
            img[p1], img[p2] = 1- img[p2],1- img[p1]
            p1 += 1
            p2 -= 1
    return image
# print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
def applyOperations(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i] == nums[i - 1]:
            nums[i] = 0
            nums[i - 1] *=2
    p1 = 0
    for i in range(n):
        if nums[i] != 0:
            nums[p1],nums[i] = nums[i],nums[p1]
            p1 += 1
    return nums
# print(applyOperations([1,2,2,1,1,0]))
# a,b = map(int,input.split())

def countOne(nums):
    d = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in d.keys():
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1
    for key,value in d.items():
        if value == 1:
            return key
# print(countOne([5, 7, 5]))
def max_algo(nums,a,m):
    nums.sort()
    sum = nums[0]
    count = 0
    for i in range(a):
        if(sum <= m):
            sum += nums[i]
            count += 1
    return count
# print(max_algo([4, 3, 8, 4, 7, 3],6, 15))
# [3,3,4,4,7,8]

def unique_song(n,songs):
    d = {}
    for i in range(n):
        if songs[i] in d.keys():
            d[songs[i]] += 1
        else:
            d[songs[i]] = 1
    return len(d)
# print(unique_song(8,[1, 2, 1, 3, 2, 7, 4, 2]))
def unique_seq(n,songs):
    p1 = 0
    max_seq = 0
    
    while(p1 < n):
        seen = []
        p2 = p1
        while p2 < n and songs[p2] not in seen:
            seen.append(songs[p2])
            p2 += 1
            max_seq = max(max_seq, p2 - p1)
        p1 += 1
    return max_seq
# print(unique_seq(8,[1, 2, 1, 3, 2, 7, 4, 2]))

def sub_arr_sum(n,t,nums):
    count = 0
    for p1 in range(n):
        sum = 0
        for p2 in range(p1,n):
            sum += nums[p2]
            if sum == t:
                count += 1
                break
    return count
# print(sub_arr_sum(5, 7,[2, 4, 1, 2, 7]))
def max_row(num):
    remaining_items = num
    row = 0
    for i in range(1,num // 2):
        remaining_items -= i
        row += 1
        if remaining_items < i:
            break
        
    return row
# print(max_row(12))
# strictly palindrome
def strictly_palindrome(num):
    for i in range(2,num-1):
        temp_num = num
        str_bin = ""
        while temp_num:
            str_bin = str(temp_num % i) + str_bin
            temp_num = temp_num // i
        if str_bin != str_bin[::-1]:
            return False
    return True
# print(strictly_palindrome(9))
def insert_sort(nums):
    n = len(nums)
    for i in range(n):
        idx = i
        for j in range(i + 1,n):
            if nums[idx] > nums[j]:
                nums[idx],nums[j] = nums[j],nums[idx]
    return nums
# print(insert_sort([2,0,2,1,1,0]))
"""
2469. Convert the Temperature
Easy

615

336

Add to List

Share
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00
"""

def convertTemperature(celsius):
    ans = []
    kelvin = round(celsius + 273.15,5)
    fahrenheit = round(celsius * 1.8 + 32.00,5)
    ans.append(kelvin)
    ans.append(fahrenheit)
    return ans
# print(convertTemperature(36.50))
def fizzBuzz(n):
        ans = []
        # loop and append the items to answer array based on condition
        for i in range(1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(f"{i}")
        return ans
# print(fizzBuzz(3))
def numIdenticalPairs(nums):
        n = len(nums)
        numOfIdentical = 0
        for i in range(n):
            for j in range(i,n):
                if nums[i] == nums[j] and i < j:
                    numOfIdentical += 1
        return numOfIdentical
# print(numIdenticalPairs([1,1,1,1]))
def IdenticalPairs(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    numOfIdentical = 0
    for value in d.values():
        if value > 1:
            numOfIdentical += (value * (value - 1)) // 2
    return numOfIdentical
# print(IdenticalPairs( [1,2,3,1,1,3]))
def finalValueAfterOperations(operations):
    x = 0
    for operation in operations:
        if operation[1] == "-":
            x -= 1
        else:
            x += 1
    return x
# print(finalValueAfterOperations(["X++","++X","--X","X--"]))
# Finding Maximum Sum Sub array of Size k
def maxSumSubArray(nums,k):
    n = len(nums)
    if n < k:
        return -1
    
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k,n):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum,current_sum)

    return max_sum
# print(maxSumSubArray([1,2,3,4,5,6],7))
def findMaxAverage(nums,k):
    n = len(nums)
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(1,n - k + 1):
        current_sum = sum(nums[i:k + i])
        max_sum = max(current_sum,max_sum)
    return max_sum / k
# print(findMaxAverage(nums = [5], k = 1))
def windowAvg(nums,k):
    n = len(nums)
    output = []
    current_sum = 0
    for i in range(k):
        current_sum += i
    current_avg = current_sum / k
    output.append(current_avg)
    for i in range(k,n):
        current_sum += nums[i] - nums[i - k]
        output.append(current_sum / k)
    return output
# print(windowAvg([1, 2, 3, 4, 5, 6, 7, 8, 9],3))
def max_sliding_window(nums, k):
    n = len(nums)
    output = []
    max_num = 0
    p1 = 0
    p2 = k
    # [1, 2, 3, 4, 5, 6, 7, 8, 9],3
    while p2 <= n:
        max_num = max(nums[p1:p2])
        output.append(max_num)
        p1 += 1
        p2 += 1
    return output
# print(max_sliding_window([1, 2, 3, 4, 5, 6, 7, 8, 9],3))
def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    
    n = len(s)
    left = 0
    right = 0
    char_count = {}
    max_length = 0
    for right in range(n):
        char = s[right]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
# print(length_of_longest_substring_k_distinct("eceba",2))
def length_of_longest_substring(s):
    n = len(s)
    start = 0
    max_length = 0
    char_set = set()
    
    for end in range(n):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
        print(char_set)
    return max_length
# print(length_of_longest_substring("abcabcbb"))
def min_subarray_len(nums,s):
    n = len(nums)
    if n == 0:
        return 0
    start = 0
    current_sum = 0
    min_length = float("inf")
    for end in range(n):
        current_sum += nums[end]
        while current_sum >= s:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    return min_length if min_length != "inf" else 0
# print(min_subarray_len([2,3,1,2,4,3],7))
def smallerThanCurrent(nums):
    sortedNums = sorted(nums)
    smallerCount = {}
    
    for i,num in enumerate(sortedNums):
        if num not in smallerCount:
            smallerCount[num] = i
    result = [smallerCount[num] for num in nums]
    return result
# print(smallerThanCurrent([8,1,2,2,3]))
def smallerThanCurrent2(nums):
    n = len(nums)
    d = {}
    for num in nums:
        d[num] = d.get(num,0) + 1
    # print(d)
    sortedNums = sorted(d.keys())
    
    cumulative_count = {}
    cumulative_sum = 0
    for n in sortedNums:
        cumulative_count[n] = cumulative_sum
        cumulative_sum += d[n]
    print(cumulative_count)
    output = []
    for num in nums:
        output.append(cumulative_count[num])
    return output
# print(smallerThanCurrent2([8,1,2,2,3]))
def arrayIntersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    p1,p2,n,m = 0,0,len(nums1), len(nums2)
    output = []
    
    while p1 < n and p2 < m:
        if nums1[p1] == nums2[p2]:
            output.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return output
# print(arrayIntersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
def maxIceCream(costs, coins):
    costs.sort()
    count_of_ice_creams = 0
    cost_of_ice_creams = 0
    
    for cost in costs:
        if cost_of_ice_creams + cost < coins:
            cost_of_ice_creams += cost
            count_of_ice_creams += 1
    return count_of_ice_creams
# print(maxIceCream([1,6,3,1,2,5],20))
def maxIceCream2(costs, coins):
    costs.sort()
    num_of_ice_creams = 0
    for c in costs:
        if c <= coins:
            num_of_ice_creams += 1
            coins -= c
        elif c > coins or coins == 0:
            break
    return num_of_ice_creams
# print(maxIceCream2(costs = [10,6,8,7,7,8], coins = 5))
import math
def distanceFromOrigin(point):
    d = math.sqrt((point[0]) ** 2 + (point[1]) ** 2)
    return d
def kClosest(points,k):
    points.sort(key=distanceFromOrigin)
    return points[:k]
# print(kClosest( points = [[3,3],[5,-1],[-2,4]], k = 2))
def kClosest2(points,k):
    distances = [(point,math.sqrt(point[0]**2 + point[1] ** 2)) for point in points]
    distances.sort(key=lambda x:x[1])
    return [point for point,distance in distances[:k]]
# print(kClosest2(points = [[3,3],[5,-1],[-2,4]], k = 2))
        
    
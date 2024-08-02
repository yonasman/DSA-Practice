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
print(targetIndices(nums = [1,2,5,2,3], target = 3))  # Expected Output: [1, 2, 3, 4]

    
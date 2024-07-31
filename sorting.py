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

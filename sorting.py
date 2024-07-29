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
print(sortDuplicates([5, 1, 3, 5, 2, 1]))
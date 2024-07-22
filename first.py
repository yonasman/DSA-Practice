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
print(common_prefix(["flower","flow","flight"]))
            

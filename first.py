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
ans = 1
for i in range(1,6):
    ans *= i
print(ans)
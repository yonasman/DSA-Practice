# Practicing stacks
from collections import deque
# initialize stack
stack = deque()
# pushing elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
# print the stack
# print(stack)
# creating custom stack class
class Stack:
    # constructor
    def __init__(self):
        self.stack = []
    # push operation
    def push(self,element):
        self.stack.append(element)
    # pop operation
    def pop(self):
        if not self.stack.is_empty(): 
            return self.pop()
        else:
            return "stack is empty"
    # peek operation
    def peek(self):
        if not self.stack.is_empty():
            return self.stack[-1]
        else:
            return "stack is empty"
    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    # return the size of stack
    def size(self):
        return len(self.stack)
stack = Stack()
stack.push(1)
# print(stack)
def stackImplementation() :
    stack = []
    for i in range(1,11):
        stack.append(i)
    print(stack)
    for i in range(10):
        print(stack.pop())
# stackImplementation()
def isValid(s):
    matching_Parenthesis = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for char in s:
        if char in matching_Parenthesis:
            top_element = stack.pop()
            if matching_Parenthesis[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
# print(isValid("()"))
# reverse a string using stack
def reverseStringWithStack(s):
    stack = []
    for char in s:
        stack.append(char)
    reversedStr = []
    for _ in range(len(s)):
        reversedStr.append(stack.pop())
    return ''.join(reversedStr)
# print(reverseStringWithStack("yonas"))
def removeDuplicates(nums):
    n = len(nums)
    stack = []
    for i in range(n):
        if not stack:
            stack.append(nums[i])
        else:
            if stack[-1] != nums[i]:
                stack.append(nums[i])
    return stack
# print(removeDuplicates([1,1,2]))
def removeDuplicates2(nums):
    uniqueStack = []
    for num in nums:
        if not uniqueStack:
            uniqueStack.append(num)
        else:
            if uniqueStack[-1] != num:
                uniqueStack.append(num)
    print(uniqueStack)
    return len(uniqueStack)
# print(removeDuplicates2([1,1,2]))
def removeDuplicates3(nums):
    n = len(nums)
    # return 0 if empty
    if not nums:
        return 0
    i = 0 
    for j in range(1,n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# print(removeDuplicates3([1,1,2]))
def maxDepth(s):
    if not s:
        return 0
    stack = []
    max_depth = 0
    # "(1+(2*3)+((8)/4))+1"
    for char in s:
        if char == '(':
            stack.append(char)
            max_depth = max(max_depth,len(stack))
        elif char == ')':
            stack.pop()
    return max_depth
# print(maxDepth("()(())((()()))"))
def maxDepth2(s):
    current_depth = 0
    max_depth = 0
    for char in s:
        if char == "(":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ")":
            current_depth -= 1
    return max_depth
# print(maxDepth2("()(())((()()))"))
def makeGood(s):
    # return empty string is s is empty
    if not s:
        return ""
    # initialize empty stack to keep track of the characters
    stack = []
    # iterate over each char of the string
    for char in s:
        # check if the stack is not empty and the top of the stack is the
        # opposite case of the current char
        if stack and stack[-1].swapcase() == char:
            # if they match, pop the top char from the stack
            stack.pop()
        else:
            # otherwise, push the char to the top of the stack
            stack.append(char)
    # join the chars in the stack to form the resulting string and return it
    return ''.join(stack)
# print(makeGood("s"))
def simplifyPath(path):
    stack = []
    pathComponents = path.split('/')
    for component in pathComponents:
        if component == '' or component == '.':
            continue
        elif component == "..":
            if stack:
                stack.pop()
        else:
            stack.append(component)
    return '/' + '/'.join(stack)
# print(simplifyPath("/.../a/../b/c/../d/./"))
def evalRPN(tokens):
    # initialize a stack to perform the operation
    stack = []
    for token in tokens:
        if token == '+':
            stack[-2] = stack[-2] + stack[-1]
            stack.pop()
        elif token == '-':
            stack[-2] = stack[-2] - stack[-1]
            stack.pop()
        elif token == '*':
            stack[-2] = stack[-2] * stack[-1]
            stack.pop()
        elif token == '/':
            stack[-2] = int(stack[-2] / stack[-1])
            stack.pop()
        else:
            stack.append(int(token))
    return stack[-1]
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
def evalRPN2(tokens):
    stack = []
    for token in tokens:
        if token not in {'+','-','*','/'}:
            stack.append(int(token))
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num2 - num1)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                if num2 * num1 < 0 and num2 % num1 != 0:
                    stack.append((num2 // num1) + 1)
                else:
                    stack.append(num2 // num1)
    return stack[-1]
# print(evalRPN2(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
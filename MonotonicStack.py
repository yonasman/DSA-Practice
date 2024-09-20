# next greater element
def nextGreaterElement(nums):
    n = len(nums)
    stack = []
    output = [-1] * n
    for i in range(n - 1,-1,-1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            output[i] = stack[-1]
        stack.append(nums[i])
    return output
# print(nextGreaterElement([1,3,2,5,4]))
def nextGreaterElement2(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result
# print(nextGreaterElement2([1,3,2,5,4]))
def dailyTemperatures(temperatures):
    # [1,1,4,2,1,1,0,0]
    n = len(temperatures)
    output = [0] * n
    for i in range(n):
        for j in range(i + 1,n):
            if temperatures[j] > temperatures[i]:
                output[i] = j - i
                break
    return output
# print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result
# print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

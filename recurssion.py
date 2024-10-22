def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n = n -1
    return product
# print(factorial(5))
def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)
# print(factorial2(3))
def oneToTen(n):
    if n == 0:
        return
    print(n)
    oneToTen(n - 1)
# oneToTen(10)
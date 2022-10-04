import math

iter = 100

def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

def my_exp(x):  # e^x
    """
    Вычисление экспоненты при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    ans = 0
    for i in range(0, iter):
        ans += x**i / factorial(i)
    return ans

help(math.exp)
help(my_exp)

# n = int(input())

print(math.exp(20))
print(my_exp(20))

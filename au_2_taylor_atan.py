import math

iter = 100

def my_atan(x):  # e^x
    """
    Вычисление арктангенса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    sum = 0
    for i in range(iter):
        pow = 2 * i + 1
        sum += ((-1) ** i) / (2 * n + 1) * x ** pow
    return sum

help(math.atan)
help(my_atan)

# n = int(input())

print(math.atan(0.2))
print(my_atan(0.2))

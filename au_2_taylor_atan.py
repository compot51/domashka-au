import math
import numpy
import matplotlib.pyplot as mpp

const = 10

def my_atan(x):
    """
    Вычисление арктангенса при помощи частичного суммирования
    ряда Тейлора для окрестности 0 при |x| < 1
    """
    sum = 0
    for i in range(const):
        pow = 2 * i + 1
        sum += ((-1) ** i) / (2 * i + 1) * x ** pow
    return sum

help(math.atan)
help(my_atan)

# n = int(input())

print(math.atan(0.2))
print(my_atan(0.2))

arg = numpy.arange(-1.5, 1.5, 0.01)

mpp.plot(arg, [my_atan(a) for a in arg], linewidth = 3.0, color = "red")
mpp.plot(arg, [math.atan(a) for a in arg], linewidth = 1.0, color = "cyan")
mpp.show()

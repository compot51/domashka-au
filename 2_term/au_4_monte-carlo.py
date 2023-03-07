# Вычисление числа π
import random
from numpy import arange

n = 100000
scal_val = 1 / n

cnt_in = 0  # Счётчик попаданий точек в круг
cnt_out = 0  # Ан-но непопаданий

for x in arange(0, 1, scal_val):
	y = random.random()
	if x ** 2 + y ** 2 <= 1:
		cnt_in += 1
	else:
		cnt_out += 1

rel = cnt_in / cnt_out
print(4 * rel / (1 + rel))  # Выводится из ур-ия соотношений площадей попадающих и непопадающих в круг точек

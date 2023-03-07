import random
from numpy import arange
from numba import jit

@jit(nopython="True")
def solve():
	n = 1000000
	scal_val = 1 / n
	cnt_in = 0
	cnt_out = 0

	for x in arange(0, 1, scal_val):
		y = random.random()
		if x ** 2 + y ** 2 <= 1:
			cnt_in += 1
		else:
			cnt_out += 1

	rel = cnt_in / cnt_out
	return 4 * rel / (1 + rel)


a = tmp = 0
t = 100

while t:
	# tmp = solve()
	a += solve()
	# print(a - tmp)
	t -= 1

print(a / 100)

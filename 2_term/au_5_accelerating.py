import random
from numpy import arange
from multiprocessing import Pool

def solve(n):
    n = 100000
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


a = 0

if __name__ == '__main__':
    with Pool(2) as p:
        a = sum(p.map(solve, list(range(100))))
    print(a / 100)

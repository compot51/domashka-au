import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    a = a.copy()
    b = b.copy()

    N = len(a)

    def forward():
        for shift in range(N):
            for i in range(shift + 1, N):
                div = a[i][shift] / a[shift][shift]
                for j in range(shift, N):
                    a[i][j] -= a[shift][j] * div
                b[i] -= b[shift] * div
            

    def backward():
        x = numpy.zeros(N, dtype=float)
        x[N - 1] = b[N - 1] / a[N - 1][N - 1]
        for i in range(N - 2, -1, -1):
            sum = 0
            for j in range(i + 1, N):
                sum += a[i][j] * x[j]
            x[i] = (b[i] - sum) / a[i][i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))

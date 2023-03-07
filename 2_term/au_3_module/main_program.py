from matrix_module import *

A = Matrix(5, 7)
A = A.set_in_a_row_length()
print("The first matrix A:\n", A, sep = '')

B = Matrix(7, 5)
B = B.set_in_a_row_length()
print("The second matrix B:\n", B, sep = '')
 
E = Matrix(5, 7)
E = E.set_id_matrix()
print("The identity matrix E (for A dimensions):\n", E, sep = '')

print("The transposing of B:\n", B.transpose(), sep = '')
print("The addition of A and transposed B:\n", A + B.transpose(), sep = '')
print("The subtraction of A and transposed B:\n", A - B.transpose(), sep = '')
print("The multiplication of A and B:\n", A * B, sep = '')

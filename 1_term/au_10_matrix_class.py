class Matrix:

	def __init__(self, length, width, fill = 0):
		self.length = length
		self.width = width
		self.matrix = [[fill] * self.width for i in range(self.length)]

	def __getitem__(self, key):
		if isinstance(key, tuple):
			i = key[0]
			j = key[1]
			return self.matrix[i][j]


	def __setitem__(self, key, value):
		if isinstance(key, tuple):
			i = key[0]
			j = key[1]
			self.matrix[i][j] = value

	def __str__(self):
		res = ""
		for i in range(len(self.matrix)):
			res += str(self.matrix[i]) + "\n"
		return res
	
	def set_in_a_row_length(self):
		res = Matrix(self.length, self.width)
		num = 1
		for i in range(self.length):
			for j in range(self.width):
				res.matrix[i][j] = num
				num += 1
		return res

	def set_in_a_row_width(self):
		res = Matrix(self.length, self.width)
		num = 1
		for i in range(self.width):
			for j in range(self.length):
				res.matrix[j][i] = num
				num += 1
		return res

	def set_id_matrix(self):
		res = Matrix(self.length, self.width)
		for i in range(self.length):
			for j in range(self.width):
				res.matrix[i][j] = 1 if i == j else 0
		return res

	def __add__(self, other):
		res = Matrix(self.length, self.width)
		if isinstance(other, (int, float)):
			for i in range(self.length):
				for j in range(self.width):
					res.matrix[i][j] = self.matrix[i][j] + other
		elif isinstance(other, Matrix):
			for i in range(self.length):
				for j in range(self.width):
					res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
			
		return res

	def __sub__(self, other):

		res = Matrix(self.length, self.width)

		if isinstance(other, (int, float)):
			for i in range(self.length):
				for j in range(self.width):
					res.matrix[i][j] = self.matrix[i][j] - other
		
		elif isinstance(other, Matrix):
			for i in range(self.length):
				for j in range(self.width):
					res.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
		return res
	
	def __mul__(self, other):
		if isinstance(other, (int, float)):
			res = Matrix(self.length, self.width)
			for i in range(self.length):
				for j in range(self.width):
					res.matrix[i][j] = self.matrix[i][j] * other
		elif isinstance(other, Matrix):
			res = Matrix(self.length, other.width)
			for i in range(self.length):
				for j in range(other.width):
					for k in range(other.length):
						res.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
		return res				

	def transpose(self):
		res = Matrix(self.width, self.length)
		for i in range(self.width):
			for j in range(self.length):
				res.matrix[i][j] = self.matrix[j][i]
		return res


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

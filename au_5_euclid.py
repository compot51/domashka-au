def euclid(a, b):  # Вход: a >= b >= 0
    if b == 0:
        return a
    return euclid(b, a % b)

class euclid_tests:
    
    def __init__(self):
        self.test1 = [255, 105]
        self.test2 = [0, 0]
        self.test3 = [28, 12]
        self.test4 = [399279, 164409] 
        
    def write_tests(self):
        print("gcd(", self.test1[0], ", ", self.test1[1],
              ") = ", euclid(self.test1[0], self.test1[1]), sep='')
        print("gcd(", self.test2[0], ", ", self.test2[1],
              ") = ", euclid(self.test2[0], self.test2[1]), sep='')
        print("gcd(", self.test3[0], ", ", self.test3[1],
              ") = ", euclid(self.test3[0], self.test3[1]), sep='')
        print("gcd(", self.test4[0], ", ", self.test4[1],
              ") = ", euclid(self.test4[0], self.test4[1]), sep='')


# a, b = map(int, input().split())
run = euclid_tests()
run.write_tests()

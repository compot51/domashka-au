from math import floor

def extended_euclid(a, b):  # Вход: a >= b >= 0
    if b == 0:
        if a == 0:
            return 0, 0, a
        return 1, 0, a
    x0, y0, d = extended_euclid(b, a % b)
    return y0, x0 - floor(a / b) * y0, d

class euclid_tests:

    
    def __init__(self):
        self.test1 = [255, 105]
        self.test2 = [0, 0]
        self.test3 = [28, 12]
        self.test4 = [399279, 164409]  

    
    def write_tests(self):
        print("Test 1: a = ", self.test1[0], ", b = ", self.test1[1], sep = '')
        print(self.test1[0], " * ", extended_euclid(self.test1[0], self.test1[1])[0], " + ",
              self.test1[1], " * ", extended_euclid(self.test1[0], self.test1[1])[1], " = ",
              extended_euclid(self.test1[0], self.test1[1])[2], sep = '')
        
        print("\nTest 2: a = ", self.test2[0], ", b = ", self.test2[1], sep = '')
        print(self.test2[0], " * ", extended_euclid(self.test2[0], self.test2[1])[0], " + ",
              self.test2[1], " * ", extended_euclid(self.test2[0], self.test2[1])[1], " = ",
              extended_euclid(self.test2[0], self.test2[1])[2], sep = '')
        
        print("\nTest 3: a = ", self.test3[0], ", b = ", self.test3[1], sep = '')
        print(self.test3[0], " * ", extended_euclid(self.test3[0], self.test3[1])[0], " + ",
              self.test3[1], " * ", extended_euclid(self.test3[0], self.test3[1])[1], " = ",
              extended_euclid(self.test3[0], self.test3[1])[2], sep = '')
        
        print("\nTest 4: a = ", self.test4[0], ", b = ", self.test4[1], sep = '')
        print(self.test4[0], " * ", extended_euclid(self.test4[0], self.test4[1])[0], " + ",
              self.test4[1], " * ", extended_euclid(self.test4[0], self.test4[1])[1], " = ",
              extended_euclid(self.test4[0], self.test4[1])[2], sep = '')
        

        
# a, b = map(int, input().split())
run = euclid_tests()
run.write_tests()

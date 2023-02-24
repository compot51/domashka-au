def fermat_test(n):
    for a in range(1, n):
        if (a ** (n - 1)) % n != 1:
            return False
    return True

class prime_tests:

    def __init__(self):
        self.test1 = 17
        self.test2 = 30
        self.test3 = 997
        self.test4 = 2_147_483

    def write_tests(self):
        print(self.test1, "is probably prime" if fermat_test(self.test1) == 1
              else "is definitely composite")
        print(self.test2, "is probably prime" if fermat_test(self.test2) == 1
              else "is definitely composite")
        print(self.test3, "is probably prime" if fermat_test(self.test3) == 1
              else "is definitely composite")
        print(self.test4, "is probably prime" if fermat_test(self.test4) == 1
              else "is definitely composite")


run = prime_tests()
run.write_tests()

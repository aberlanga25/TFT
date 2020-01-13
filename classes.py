class operations():

    def isTriangular(self, num):
        if (num < 0):
            return False
        sum, n = 0, 1
        while (sum <= num):
            sum = sum + n
            if (sum == num):
                return False
            n += 1
        return True

    def check_item_base(self, num):
        if self.isTriangular(num):
            n = 0
            while (self.isTriangular(num - n)):
                n += 1
            return n

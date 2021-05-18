class Solution:

    @staticmethod
    def getNthUglyNo(n):
        # code here
        result = 0
        num = 1
        count = 1
        while (count < n):
            num = num + 1
            if (Solution.check(num) == 1):
                result = num
                count += 1
        return result

    @staticmethod
    def check(x):
        if (x % 2 == 0):
            return Solution.check(x/2)
        else:
            if (x % 3 == 0):
                return Solution.check(x/3)
            else:
                if (x % 5 == 0):
                    return Solution.check(x/5)
                else:
                    return x


print(Solution.getNthUglyNo(150))

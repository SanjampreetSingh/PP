import math


# 01. Find the number of digits in a number
class Solution:
    def iterative_methods(self, number: int) -> int:
        count = 0
        while int(number) != 0:
            count += 1
            number /= 10
        return count

    def recursive_methods(self, number: int) -> int:
        if int(number) == 0:
            return 0
        return 1 + self.recursive_methods(number / 10)

    def logarithmic_methods(self, number: int) -> int:
        return math.floor(math.log(number, 10) + 1)


if __name__ == "__main__":
    s = Solution()
    print(s.iterative_methods(123))
    print(s.recursive_methods(122))
    print(s.logarithmic_methods(123))

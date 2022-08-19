# 03. Find the factorial of a number
from math import factorial


class Solution:
    def iterative_method(self, number: int) -> int:
        """
        :type number: int
        :rtype: int
        """
        fact = 1
        while number != 0:
            fact *= number
            number -= 1

        return fact

    def recursive_methods(self, number: int) -> int:
        """
        :type number: int
        :rtype: int
        """
        if number == 0:
            return 1

        return number * self.recursive_methods(number - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.iterative_method(4))
    print(s.recursive_methods(4))

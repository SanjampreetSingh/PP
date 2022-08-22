from array import array
import numbers


class Solution:
    def is_prime(self, number: int) -> bool:
        """
        :type number: int
        :rtype: bool
        """
        if number <= 1:
            return False

        if number == 2 or number == 3:
            return True

        if number % 2 == 0 or number % 3 == 0:
            return False

        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6

        return True

    def naive_solution(self, number: int) -> array:
        i = 2
        arr = []
        while i <= number:
            if self.is_prime(i):
                factor = i
                while number % factor == 0:
                    arr.append(i)
                    factor *= i
            i += 1

        return arr

    def efficient_solution(self, number: int) -> array:
        arr = []
        i = 2

        if number <= 1:
            return arr

        while i * i < number:
            while number % i == 0:
                arr.append(i)
                number //= i
            i += 1

        if number > 1:
            arr.append(number)

        return arr

    def more_efficient_solution(self, number: int) -> array:
        """
        This function has time complexity of O (sqrt number)
        """
        arr = []
        i = 5

        if number <= 1:
            return arr

        while number % 2 == 0:
            arr.append(2)
            number //= 2

        while number % 3 == 0:
            arr.append(3)
            number //= 3

        while i * i <= number:
            while number % i == 0:
                arr.append(i)
                number //= i
            while number % (i + 2) == 0:
                arr.append(i)
                number = number // (i + 2)
            i += 6

        if number > 3:
            arr.append(number)

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(12))
    print(s.efficient_solution(13))
    print(s.more_efficient_solution(450))

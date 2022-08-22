class Solution:
    def naive_solution(self, number: int) -> bool:
        """
        :type number:int
        :rtype:bool

        Here worst case scenario is when number is prime and we have to loop
        through all the numbers from 2 till number - 1.
        Time Complexity is O(number)
        """
        if number <= 1:
            return False

        i = 2
        while i < number:
            if number % i == 0:
                return False
            i += 1

        return True

    def optimized_solution(self, number: int) -> bool:
        """
        :type number:int
        :rtype:bool

        Here we are using the approach that every number have their factors in pair.
        So, instead of traversing all the numbers from 2 till number - 1, we just
        traverse till sqrt(number).
        Time Complexity is O(sqrt of number)
        """
        if number <= 1:
            return False

        i = 2

        while i * i < number:
            if number % i == 0:
                return False
            i += 1

        return True

    def further_optimized_solution(self, number: int) -> bool:
        """
        :type number:int
        :rtype:bool

        Here we are using the above approach but with some constraints like
        divisible by 2 and 3 numbers can be skipped in traversal.

        This is a good approach in case the number 10^9 size i.e. very large number.
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


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(2))
    print(s.optimized_solution(65))
    print(s.further_optimized_solution(130112312312))

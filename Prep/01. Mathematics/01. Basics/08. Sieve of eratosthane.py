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

    def naive_solution(self, number: int) -> list:
        """
        :type number: int
        :rtype: list
        Time Complexity is O(number * sqrt(number))
        """
        arr = []
        for i in range(1, number + 1):
            if self.is_prime(i):
                arr.append(i)

        return arr

    def sieve_of_eratosthenes(self, number: int) -> list:
        """
        :type number: int
        :rtype: list
        Time Complexity is O(number * log(log(number)))
        """
        prime = [True for i in range(number + 1)]
        i = 2
        while i <= number:
            if prime[i]:
                j = i * i
                while j <= number:
                    prime[j] = False
                    j += i
            i += 1

        arr = []
        for p in range(2, len(prime)):
            if prime[p]:
                arr.append(p)

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(23))
    print(s.sieve_of_eratosthenes(23))

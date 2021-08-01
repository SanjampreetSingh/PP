class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        primes = [True] * (n)
        i = 2
        primes[0] = False
        primes[1] = False
        count = 0

        while (i*i) <= n:
            if primes[i]:
                for val in range(i*i, n, i):
                    if primes[val]:
                        primes[val] = False
            i += 1

        for i in range(n):
            if primes[i]:
                count += 1

        return count

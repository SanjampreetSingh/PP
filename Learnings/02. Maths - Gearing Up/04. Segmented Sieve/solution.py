import math
from typing import Set


class Solution:
    def sieve_of_eratosthenes(self, n: int) -> Set:
        primes = [True] * (n+1)
        prime_set = set()

        primes[0] = False
        primes[1] = False
        i = 2

        while i*i < n+1:
            if primes[i]:
                for val in range(i*i, n+1, i):
                    if primes[val]:
                        primes[val] = False
            i += 1

        for p in range(n+1):
            if primes[p]:
                prime_set.add(p)
        return prime_set

    def get_primes(self, l: int, r: int, primes: Set) -> Set:
        gap = r-l+1
        is_primes = [True]*gap
        is_primes_set = set()

        for i in primes:
            k = math.ceil((l*1.0)/i)
            j = max(2, k)
            while i*j <= r:
                is_primes[(i*j) - l] = False
                j += 1

        for p in range(gap):
            if is_primes[p]:
                is_primes_set.add(p+l)

        return is_primes_set


if __name__ == "__main__":
    L = 10**10
    R = (10**10) + 500
    upper_limit = int(math.sqrt(R))
    obj = Solution()
    primes_set = obj.sieve_of_eratosthenes(upper_limit)
    print(obj.get_primes(L, R, primes_set))

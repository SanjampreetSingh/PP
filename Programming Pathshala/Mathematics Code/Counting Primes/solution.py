from typing import List


class Solution:
    def sieve(self, n: int = 10**6) -> List:
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        i = 2
        count = 0
        while i*i <= n+1:
            if primes[i]:
                for val in range(i*i, n+1, i):
                    primes[val] = False
            i += 1

        for i in range(0, n+1):
            if primes[i]:
                count += 1
            primes[i] = count

        return primes


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    lst = obj.sieve()
    for _ in range(T):
        print(lst[int(input())])

# User function Template for python3
import math


class Solution:
    def primeProduct(self, L, R):
        n = math.ceil(math.sqrt(R))
        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False
        i = 2

        while (i*i <= n + 1):
            if primes[i]:
                for val in range(i*i, n + 1, i):
                    if primes[val]:
                        primes[val] = False
            i += 1

        primes_set = set()
        for j in range(n+1):
            if primes[j]:
                primes_set.add(j)

        gap = R - L + 1
        is_prime = [True]*gap
        mod = 10**9 + 7

        for i in primes_set:
            k = math.ceil((L*1.0)/i)
            j = max(2, k)
            while i*j <= R:
                is_prime[(i*j)-L] = False
                j += 1

        ans = 1
        for p in range(gap):
            if is_prime[p]:
                ans *= p+L

        return (ans % mod)


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.primeProduct(L, R))
# } Driver Code Ends

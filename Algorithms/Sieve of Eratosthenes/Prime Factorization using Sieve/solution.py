from typing import List


class Solution:
    # Calculating SPF (Smallest Prime Factor)
    # for every number till MAX-N.
    # Time Complexity : O(n*(log(log(n))))
    def sieve(self, n: int) -> List:
        spf = [1]*(n+1)
        spf[1] = 0
        i = 2
        while (i*i <= n+1):
            if spf[i] == 1:
                for j in range(i*i, n+1, i):
                    if spf[j] == 1:
                        spf[j] = i
            i += 1
        return spf

    # A O(log n) function returning prime
    # factorization by dividing by smallest
    # prime factor at every step
    def getFactorization(self, num: int, spf: List) -> str:
        ans = ""
        while (spf[num] != 1):
            ans += str(spf[num]) + " "
            num //= spf[num]

        if num != 1:
            ans += str(num)

        return ans


# Driver code
if __name__ == '__main__':
    obj = Solution()
    # precalculating Smallest Prime Factor
    spf = obj.sieve(100001)
    num = 12246
    print("prime factorization for", num, ": ", end="")

    # calling getFactorization function
    ans = obj.getFactorization(num, spf)
    print(ans, end=" ")

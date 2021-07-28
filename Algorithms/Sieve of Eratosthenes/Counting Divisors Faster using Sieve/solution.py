from typing import List


class Solution:
    # Calculating SPF (Smallest Prime Factor)
    # for every number till N.
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

# A O(log n) function returning
# count of factors
# by dividing by smallest
# prime factor at every step
def getFactorCount(self, num: int, spf: List) -> int:

    temp = spf[num]
    count = 0
    ans = 1

    # loop for factorization
    while (spf[num] != 1):
        #  condition for count manupulation
        if temp == spf[num]:
            count += 1
        else:
            count += 1
            # ans cal
            ans *= count
            temp = spf[num]
            count = 1
        # division
        num //= spf[num]

    # count for last number that loop came out for
    count += 1
    ans *= count

    # count for number on right side of root num
    if num != 1:
        count = 2
        ans *= count

    return ans


# Driver code
if __name__ == '__main__':
    obj = Solution()
    # precalculating Smallest Prime Factor
    spf = obj.sieve(100001)
    num = 6060
    print("Number of factor of", num, "are: ", end="")

    # calling getFactorCount function
    ans = obj.getFactorCount(num, spf)
    print(ans, end=" ")

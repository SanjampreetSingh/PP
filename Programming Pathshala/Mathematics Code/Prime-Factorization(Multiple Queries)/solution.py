from typing import List


class Solution:
    def sieve(self, n: int = 10**6) -> List:
        spf = [1]*(n+1)
        spf[0] = 0
        spf[1] = 0
        i = 2

        while i*i <= (n+1):
            if spf[i]:
                for j in range(i*i, n+1, i):
                    if spf[j] == 1:
                        spf[j] = i
            i += 1

        return spf

    def getPrimeFactor(self, num: int, spf: List) -> int:

        temp = spf[num]
        count = 0

        # loop for factorization
        while (spf[num] != 1):
            if temp == spf[num]:
                count += 1
            else:
                print(temp, count)
                temp = spf[num]
                count = 1
            num //= spf[num]
            if spf[num] == 1:
                if temp != num:
                    print(temp, count)
                    temp = spf[num]

        if num != 1:
            if num == temp:
                print(temp, count+1)
            else:
                print(num, 1)


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    lst = obj.sieve()
    for _ in range(T):
        obj.getPrimeFactor(int(input()), lst)

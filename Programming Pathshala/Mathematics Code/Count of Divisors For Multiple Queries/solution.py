from typing import List


class Solution:
    def sieve(self, n: int = 10**6) -> List:
        spf = [1]*(n+1)
        spf[0] = 0
        spf[1] = 0
        i = 2

        while i*i <= (n+1):
            if spf[i] == 1:
                for j in range(i*i, n+1, i):
                    if spf[j] == 1:
                        spf[j] = i
            i += 1

        return spf

    def getPrimeFactorFactorCount(self, input_lst: List, spf: List) -> List:
        output_lst = []
        for num in input_lst:
            arr = []

            # loop for factorization
            while (spf[num] != 1):
                arr.append(spf[num])
                num //= spf[num]

            # count for number on right side of root num
            if num != 1:
                arr.append(num)
            output_lst.append(len(set(arr)))
        return output_lst


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    lst = obj.sieve()
    for _ in range(T):
        N = int(input())
        output_lst = obj.getPrimeFactorFactorCount(
            list(map(int, input().strip().split()))[:N], lst)
        listToStr = ' '.join(map(str, output_lst))
        print(listToStr)

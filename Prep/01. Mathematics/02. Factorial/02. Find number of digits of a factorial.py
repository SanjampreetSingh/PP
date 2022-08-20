import math


class Solution:
    def digitsInFactorial(self, N):
        res = 0
        for i in range(2, N + 1):
            res += math.log10(i)
        return int(math.floor(res) + 1)


def main():
    T = int(input())

    while T > 0:
        N = int(input())
        ob = Solution()
        print(ob.digitsInFactorial(N))

        T -= 1


if __name__ == "__main__":
    main()

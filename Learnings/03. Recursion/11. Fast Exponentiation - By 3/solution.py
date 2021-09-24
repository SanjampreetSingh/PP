import math


class Solution:

    def fast_exponentiation(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        val = self.fast_exponentiation(n, k//3)
        if k % 3 == 0:
            val *= val * val
        else:
            i = k % 3
            val *= val * val * n**i

        return val


if __name__ == "__main__":
    obj = Solution()
    print(obj.fast_exponentiation(2, 500000))

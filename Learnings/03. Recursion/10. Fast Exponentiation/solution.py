import math


class Solution:

    def fast_exponentiation(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        val = self.fast_exponentiation(n, k//2)
        if k % 2 != 0:
            val *= n * val
        else:
            val *= val

        return val


if __name__ == "__main__":
    obj = Solution()
    print(obj.fast_exponentiation(2, 5000))

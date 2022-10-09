import math


class Solution:
    def reverse_integer(self, value: int) -> int:
        reverse: int = 0
        temp = value
        if temp < 0:
            temp = -1 * (temp)
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp //= 10
        if value < 0:
            return -1 * reverse
        return reverse


if __name__ == "__main__":
    s = Solution()
    print(s.reverse_integer(-340))

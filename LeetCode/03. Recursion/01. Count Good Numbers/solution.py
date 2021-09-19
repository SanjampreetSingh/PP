import math


class Solution:
    def power(self, x: int, y: int, mod: int) -> int:
        if y == 0:
            return 1

        r = self.power(x, y//2, mod)

        ans = ((r % mod) * (r % mod)) % mod

        if y % 2 == 0:
            return ans
        return ((ans) * (x % mod)) % mod

    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        pass2 = 1
        pass1 = self.power(5, math.ceil(n/2.0), mod)
        if n > 1:
            pass2 = self.power(4, n//2, mod)

        return ((pass1) * (pass2)) % mod

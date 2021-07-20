import math
from typing import List


class Solution:
    def listOfDivisors(self, val: int, sqrt: int) -> List:
        count = 0
        ret = 0
        for i in range(1, sqrt+1):
            if (val % i == 0):
                ret += i
                ret += val//i
                count += 2
        if count == 4:
            return ret
        return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            sqrt = int(math.sqrt(i))
            if (sqrt*sqrt != i):
                ans += self.listOfDivisors(i, sqrt)
        return ans

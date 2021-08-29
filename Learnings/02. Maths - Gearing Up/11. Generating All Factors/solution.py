from typing import List
import math


class Solution:
    def generating_all_factors(self, n: int) -> List:
        ans = []
        for i in range(1, int(math.sqrt(n))+1):
            if (n % i == 0):
                if i*i == n:
                    ans.append(i)
                else:
                    ans.append(i)
                    ans.append(n//i)

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.generating_all_factors(16))

from typing import List


class Solution:
    def gcd(self, a: int, b: int) -> int:
        max_m = max(a, b)
        min_m = min(a, b)

        if min_m == 0:
            return max_m

        while (max_m % min_m != 0):
            temp = max_m
            max_m = min_m
            min_m = temp % min_m

        return min_m

    def gcd_array(self, input_arr: List) -> List:
        n = len(input_arr)
        if n > 1:
            ans = self.gcd(input_arr[0], input_arr[1])

        if n > 2:
            for i in range(2, n):
                ans = self.gcd(ans, input_arr[i])

        return ans

if __name__ == "__main__":
    obj = Solution()
    array = [12, 18, 20]
    print(obj.gcd_array(array))

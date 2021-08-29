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


if __name__ == "__main__":
    obj = Solution()
    print(obj.gcd(7, 25))

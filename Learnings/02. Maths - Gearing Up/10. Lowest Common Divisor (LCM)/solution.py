class Solution:
    def gcd(self, a: int, b: int) -> int:
        min_m = min(a, b)
        max_m = max(a, b)

        if min_m == 0:
            return max_m

        while (max_m % min_m != 0):
            temp = max_m
            max_m = min_m
            min_m = temp % min_m

        return min_m

    def lcm(self, a: int, b: int) -> int:
        return ((a*b)//self.gcd(a, b))


if __name__ == "__main__":
    obj = Solution()
    print(obj.lcm(12, 18))

class Solution:
    def common_divisors(self, a: int, b: int) -> int:
        max_v = max(a, b)
        min_v = min(a, b)
        count = 0

        if min_v == 0:
            return 1
        i = 1
        while(i*i <= min_v):
            if (min_v % i == 0 and max_v % i == 0):
                count += 1
            if (min_v % (min_v//i) == 0 and max_v % (min_v//i) == 0):
                count += 1
            i += 1
        return count


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    for _ in range(T):
        a, b = map(int, input().split())
        print(obj.common_divisors(a, b))

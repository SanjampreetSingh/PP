class Solution:
    def gcd(self, a, b):
        max_val = max(a, b)
        min_val = min(a, b)

        if (min_val == 0):
            return max_val

        while (max_val % min_val != 0):
            temp = max_val
            max_val = min_val
            min_val = temp % min_val

        return min_val

    def lcm_ab(self, a, b):
        return ((a*b)//self.gcd(a, b))

    def special_contest(self, n, a, b, k):
        val = int((n//a)+(n//b)-(2*(n//(self.lcm_ab(a, b)))))
        if val >= k:
            print("Win")
        else:
            print("Lose")


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, a, b, k = map(int, input().split())
        obj = Solution()
        obj.special_contest(n, a, b, k)

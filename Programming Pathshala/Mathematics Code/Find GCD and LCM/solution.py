# User function Template for python3
class Solution:
    def gcd_and_lcm(self, a, b):
        max_val = max(a, b)
        min_val = min(a, b)
        if (min_val == 0):
            gdc = max_val
        else:
            while (max_val % min_val != 0):
                temp = max_val
                max_val = min_val
                min_val = temp % min_val
            gcd = min_val
        lcm = ((a*b)//gcd)
        print(gcd, lcm)


if __name__ == '__main__':
    a, b = map(int, input().split())
    obj = Solution()
    obj.gcd_and_lcm(a, b)

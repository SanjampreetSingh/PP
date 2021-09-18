# User function Template for python3

import math


class Solution:
    def lcmAndGcd(self, a, b):
        # code here
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
        return [lcm, gcd]

# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
# } Driver Code Ends

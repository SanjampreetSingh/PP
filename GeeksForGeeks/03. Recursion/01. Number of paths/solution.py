# User function Template for python3

class Solution:
    def numberOfPaths(self, n, m):
        if m == 1 or n == 1:
            return 1
        return self.numberOfPaths(n, m-1) + self.numberOfPaths(n-1, m)


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)


# } Driver Code Ends

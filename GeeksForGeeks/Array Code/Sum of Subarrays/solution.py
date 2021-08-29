# User function Template for python3

class Solution:
    def subarraySum(self, a, n):
        # code here
        ans = 0
        m = 10**9+7

        for i in range(0, n):
            contribution = (((i+1) % m * (n-i) % m) % m * a[i] % m) % m
            ans = (ans % m + contribution % m) % m

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3
def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.subarraySum(a, n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends

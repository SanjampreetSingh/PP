# User function Template for python3

def minSwap(arr, n, k):
    if 1 <= n < 10**5:
        # Complete the function
        window_size = 0
        legal_count_in_each_window = 0
        max_legal_count = 0

        for i in arr:
            if i <= k:
                window_size += 1

        for i in range(0, window_size):
            if arr[i] <= k:
                max_legal_count += 1
                legal_count_in_each_window += 1

        for i in range(window_size, n):
            if arr[i-window_size] <= k:
                legal_count_in_each_window -= 1
            if arr[i] <= k:
                legal_count_in_each_window += 1
            if legal_count_in_each_window > max_legal_count:
                max_legal_count = legal_count_in_each_window

        return max_legal_count


# {
#  Driver Code Starts
# Initial Template for Python 3
for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
# } Driver Code Ends

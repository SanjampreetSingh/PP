from typing import List


class Solution:
    # returns new array
    def prefix_sum(self, n: int, arr: List) -> List:
        i = 1
        prefix_arr = [0]*n
        prefix_arr[0] = arr[0]
        while i < n:
            prefix_arr[i] = prefix_arr[i-1] + arr[i]
            i += 1

        return prefix_arr

    # returns updated array
    def prefix_sum_modify_input(self, n: int, arr: List) -> List:
        i = 1
        while i < n:
            arr[i] = arr[i-1] + arr[i]
            i += 1

        return arr


# Driver Code
if __name__ == '__main__':
    arr = []

    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    obj = Solution()
    output = obj.prefix_sum(n, arr)
    output1 = obj.prefix_sum_modify_input(n, arr)
    print(output, output1)

from typing import List


class Solution:
    def prefix_max(self, arr_input: List) -> List:
        len_arr = len(arr_input)
        prefix_arr = [0]*len_arr
        prefix_arr[0] = arr_input[0]

        for i in range(1, len_arr):
            prefix_arr[i] = max(prefix_arr[i-1], arr_input[i])

        return prefix_arr


if __name__ == "__main__":
    arr_input = [21, 3, 55, 63, 125, 63, 7, 31, 63, 78, 631, 53]
    obj = Solution()
    print(obj.prefix_max(arr_input))

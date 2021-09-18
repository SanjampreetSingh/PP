from typing import List


class Solution:

    def sliding_window_sum(self, input_arr: List, k: int) -> int:
        n = len(input_arr)
        sum_window = sum(input_arr[:k])
        print(sum_window)
        for i in range(k, n):
            sum_window += input_arr[i] - input_arr[i-k]
            print(sum_window)


if __name__ == "__main__":
    obj = Solution()
    input_arr = [2, 1, 0, 4, 3, 5]
    obj.sliding_window_sum(input_arr, 3)

from typing import List


class Solution:

    def sliding_window_frequency_counter(self, input_arr: List, k: int, x: int) -> int:
        n = len(input_arr)
        freq = 0
        for i in input_arr[:k]:
            if i == x:
                freq += 1
        print(freq)

        for i in range(k, n):
            if x == input_arr[i]:
                freq += 1
            if x == input_arr[i-k]:
                freq -= 1
            print(freq)


if __name__ == "__main__":
    obj = Solution()
    input_arr = [2, 2, 1, 2, 4, 6, 2]
    obj.sliding_window_frequency_counter(input_arr, 4, 2)

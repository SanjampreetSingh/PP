from typing import List


class Solution:
    def histogram_problem(self, input_arr: List) -> int:
        len_arr = len(input_arr)

        prefix_max = [0]*len_arr
        prefix_max[0] = input_arr[0]
        for i in range(1, len_arr):
            prefix_max[i] = max(prefix_max[i-1], input_arr[i])

        suffix_max = [0]*len_arr
        suffix_max[len_arr-1] = input_arr[len_arr-1]
        for i in range(len_arr-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], input_arr[i])

        water_collected = 0
        for i in range(1, len_arr-1):
            deciding_height = min(prefix_max[i-1], suffix_max[i+1])
            if (deciding_height > input_arr[i]):
                water_collected += deciding_height - input_arr[i]

        return water_collected


if __name__ == "__main__":
    arr_input = [21, 3, 55, 613, 7, 31, 63, 78, 53]
    obj = Solution()
    print(obj.histogram_problem(arr_input))

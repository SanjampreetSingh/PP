from typing import List


class Solution:
    def suffix_sum(self, arr_input: List) -> List:
        len_arr = len(arr_input)
        suffix_arr = [0]*len_arr
        suffix_arr[len_arr-1] = arr_input[len_arr-1]

        for i in range(len_arr-2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] + arr_input[i]

        return suffix_arr


if __name__ == "__main__":
    arr_input = [21, 3, 55, 613, 7, 31, 63, 78, 53]
    obj = Solution()
    print(obj.suffix_sum(arr_input))

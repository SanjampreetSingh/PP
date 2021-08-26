from typing import List


class Solution:
    def maximize_the_expression(self, input_arr: List, p: int, q: int, r: int) -> int:
        len_arr = len(input_arr)

        pre_max = [0]*len_arr
        pre_max[0] = p*input_arr[0]
        for i in range(1, len_arr):
            pre_max[i] = max(pre_max[i-1], p*input_arr[i])

        ans = 0
        suf_max = r*input_arr[len_arr - 1]
        for i in range(len_arr-2, -1, -1):
            suf_max = max(suf_max, r*input_arr[i])
            ans = max(ans, (pre_max[i-1] + (q*input_arr[i]) + suf_max))
        return ans


if __name__ == "__main__":
    p, q, r = 1, 2, 3
    input_arr = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.maximize_the_expression(input_arr, p, q, r))

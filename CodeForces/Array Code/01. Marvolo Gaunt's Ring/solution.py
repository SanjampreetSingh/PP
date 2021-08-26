from typing import List


class Solution:
    def maximize_expression(self, input_arr: List, n: int, p: int, q: int, r: int) -> int:

        pre_max = [0] * n
        pre_max[0] = p*input_arr[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], p*input_arr[i])

        suf_max = [0] * n
        suf_max[n-1] = r*input_arr[n-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], r*input_arr[i])

        ans = -1e20
        for i in range(n):
            ans = max(ans, pre_max[i] + q*input_arr[i] + suf_max[i])

        return ans


if __name__ == "__main__":
    n, p, q, r = map(int, input().split())
    input_arr = list(map(int, input().strip().split()))[:n]
    obj = Solution()
    print(obj.maximize_expression(input_arr, n, p, q, r))

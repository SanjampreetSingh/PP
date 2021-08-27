from typing import List


class Solution:
    def can_be_chunked(self, i: int, j: int, input_arr: List) -> bool:
        count = 0
        for k in range(i, j+1):
            if (input_arr[k] >= i and input_arr[k] <= j):
                count += 1

        return (count == (j - i + 1))

    def max_chunks(self, input_arr: List) -> int:
        i, ans = 0, 0
        n = len(input_arr)

        while i < n:
            for j in range(i, n):
                if (self.can_be_chunked(i, j, input_arr)):
                    break
            i = j + 1
            ans += 1

        return ans


if __name__ == "__main__":
    obj = Solution()
    input_arr = [0, 1, 2, 3]
    print(obj.max_chunks(input_arr))

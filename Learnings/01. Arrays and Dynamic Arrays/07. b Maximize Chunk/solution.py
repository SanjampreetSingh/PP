from typing import List


class Solution:

    def max_chunks(self, input_arr: List) -> int:
        i, ans, current_max, n = 0, 0, -1e20, len(input_arr)

        while i < n:
            current_max = max(current_max, input_arr[i])
            if i == current_max:
                ans += 1
            i += 1

        return ans


if __name__ == "__main__":
    obj = Solution()
    input_arr = [2, 1, 0, 4, 3, 5]
    print(obj.max_chunks(input_arr))

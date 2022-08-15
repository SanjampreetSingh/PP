# 01. Find the only non-repeating element in the array where every element is repeated twice.


class Solution:
    def non_repeating(self, arr: list) -> int:
        result = 0
        for i in arr:
            result ^= i
        return result


if __name__ == "__main__":
    arr = [5, 4, 1, 3, 2, 3, 5, 4, 1]
    obj = Solution()
    print(obj.non_repeating(arr))

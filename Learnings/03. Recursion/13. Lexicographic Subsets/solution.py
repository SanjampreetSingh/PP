from typing import List


class Solution:
    def lexicographic_subsets(self, n: int, ele: int, idx: int, arr: List[int], size: int) -> None:
        print(ele[:size])
        if idx == n:
            return

        for i in range(idx, n):
            ele[size] = arr[i]
            self.lexicographic_subsets(n, ele, i+1, arr, size+1)


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 3, 4]
    n = len(arr)
    obj.lexicographic_subsets(n, [0]*n, 0, arr, 0)

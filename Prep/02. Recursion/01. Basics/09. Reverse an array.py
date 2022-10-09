class Solution:
    def reverse_array(self, arr: list, start: int, end: int) -> list:
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            self.reverse_array(arr, start + 1, end - 1)
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.reverse_array([1, 2, 3, 4, 5], 0, 4))


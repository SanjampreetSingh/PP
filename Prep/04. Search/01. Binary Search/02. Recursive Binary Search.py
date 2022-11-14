class Solution:
    def binary_search(self, arr: list, element: int, low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (high + low) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return self.binary_search(arr, element, low, mid - 1)
        else:
            return self.binary_search(arr, element, mid + 1, high)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    element = 8
    s = Solution()
    print(s.binary_search(arr, element, 0, len(arr)-1))

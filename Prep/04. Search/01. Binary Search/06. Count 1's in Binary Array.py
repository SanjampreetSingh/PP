class Solution:
    def first_occurrences(self, arr):
        arr.reverse()
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < 1:
                low = mid + 1
            else:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    return mid
                else:
                    high = high - 1

        return -1

    def count_ones(self, arr: list) -> int:
        start = self.first_occurrences(arr)
        if start < 0:
            return 0
        return len(arr) - start


if __name__ == "__main__":
    s = Solution()
    print(s.count_ones([1, 1, 1, 1]))

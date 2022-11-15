class Solution:
    def index_of_last_occurance(self, arr: list, element: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > element:
                high = mid - 1
            elif arr[mid] < element:
                low = mid + 1
            else:
                if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                    return mid
                else:
                    low = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.index_of_last_occurance([1, 2, 3, 3, 3, 4, 5, 6, 7], 3))

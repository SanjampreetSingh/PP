class Solution:
    def index_of_first_occurance(self, arr: list, element: int) -> int:
        low = 0
        high = len(arr) - 1
        while high >= low:
            mid = (high + low) // 2
            if arr[mid] < element:
                low = mid + 1
            elif arr[mid] > element:
                high = mid - 1
            else:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    return mid
                else:
                    high = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.index_of_first_occurance([1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6], 10))

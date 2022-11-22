class Solution:
    def bubble_sort(self, arr: list) -> list:
        for i in range(len(arr) - 1):
            for j in range(i, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def bubble_sort_optimized(self, arr: list) -> list:
        for i in range(len(arr) - 1):
            swapped = False
            for j in range(i, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if swapped == False:
                return arr

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.bubble_sort([2, 10, 8, 6]))
    print(s.bubble_sort_optimized([2, 10, 8, 6]))

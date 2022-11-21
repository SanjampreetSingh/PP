class Solution:
    def bubble_sort(self, arr: list) -> list:
        for i in range(len(arr) - 1):
            for j in range(i, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.bubble_sort([2, 10, 8, 6]))

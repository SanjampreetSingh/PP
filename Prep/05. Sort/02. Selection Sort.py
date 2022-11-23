class Solution:
    def selection_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.selection_sort([30, 10, 5, 77]))

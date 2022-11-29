class Solution:
    def merge_sort(self, arr: list, low: int, high: int) -> list:
        while high > low:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            left = arr[low : mid + 1]
            right = arr[mid + 1 : high + 1]
            m = len(left)
            n = len(right)
            i, j = 0, 0
            k = low
            while i < m and j < n:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    k += 1

            while i < m:
                arr[k] = left[i]
                i += 1
                k += 1

            while j < n:
                arr[k] = right[j]
                j += 1
                k += 1

            return arr


if __name__ == "__main__":
    s = Solution()
    print(s.merge_sort([15, 5, 30, 10, 7], 0, 4))

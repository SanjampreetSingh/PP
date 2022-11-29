class Solution:
    def merge_two_sorted_sub_arrays(
        self, arr: list, low: int, mid: int, high: int
    ) -> list:
        left = arr[:mid+1]
        right = arr[mid+1:]
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
    print(s.merge_two_sorted_sub_arrays([4, 5, 1, 2, 3], 0, 1, 4))

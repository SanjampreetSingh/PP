class Solution:
    def insertion_sort(self, arr: list) -> list:
        for i in range(1, len(arr)):
            val = arr[i]
            j = i - 1
            while j >= 0 and val < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = val

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.insertion_sort([5, 4, 3, 2, 1]))

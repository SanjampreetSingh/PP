class Solution:
    def intersection_of_two_arrays(self, arr1: list, arr2: list):
        i, j = 0, 0
        m = len(arr1)
        n = len(arr2)

        while i < m and j < n:
            if i > 0 and arr1[i] == arr1[i - 1]:
                i += 1
                continue
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                print(arr1[i], end=" ")
                i += 1
                j += 1


if __name__ == "__main__":
    s = Solution()
    s.intersection_of_two_arrays([1, 2, 3, 3, 4], [2, 3, 4])

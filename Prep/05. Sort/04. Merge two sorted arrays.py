class Solution:
    def merge_two_sorted_arrays(self, arr1: list, arr2: list) -> list:
        n = len(arr1)
        m = len(arr2)
        i, j = 0, 0
        res = []
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1

        while i < n:
            res.append(arr1[i])
            i += 1
        while j < m:
            res.append(arr2[j])
            j += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge_two_sorted_arrays([1, 2, 3, 4], [1, 3, 4]))

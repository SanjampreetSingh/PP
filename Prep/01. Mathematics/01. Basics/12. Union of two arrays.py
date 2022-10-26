class Solution:
    def union_of_two_arrays(self, arr1, arr2):
        arr1 += arr2
        return len(set(arr1))


if __name__ == "__main__":
    s = Solution()
    print(s.union_of_two_arrays([1, 2, 3], [1, 2, 3, 4]))

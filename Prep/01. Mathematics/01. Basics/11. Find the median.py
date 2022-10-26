class Solution:
    def find_median(self, arr: list) -> int:
        arr.sort()
        if len(arr) % 2 != 0:
            return arr[len(arr) // 2]
        else:
            return (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) // 2


if __name__ == "__main__":
    s = Solution()
    print(s.find_median([56, 67, 30, 79]))

class Solution:
    def check_sorted_array(self, array: list) -> bool:

        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.check_sorted_array([8, 10, 30, 2]))

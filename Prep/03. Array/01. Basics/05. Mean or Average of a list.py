class Solution:
    def average_of_list(self, lst: list) -> float:
        return sum(lst) / len(lst)


if __name__ == "__main__":
    s = Solution()
    print(s.average_of_list([10, 20, 30, 40]))

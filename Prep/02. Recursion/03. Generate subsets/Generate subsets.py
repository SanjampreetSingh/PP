class Solution:
    def generate_subset(self, string_set: str, current_str: str = "", index: int = 0):
        if index == len(string_set):
            print(current_str)
            return
        self.generate_subset(string_set, current_str, index + 1)
        self.generate_subset(string_set, current_str + string_set[index], index + 1)


if __name__ == "__main__":
    s = Solution()
    s.generate_subset("abc")

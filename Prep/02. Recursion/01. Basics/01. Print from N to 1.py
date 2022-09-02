class Solution:
    def print_n_to_1(self, n: int) -> int:
        print(n)
        if n == 1:
            return
        self.print_n_to_1(n - 1)


if __name__ == "__main__":
    s = Solution()
    s.print_n_to_1(10)

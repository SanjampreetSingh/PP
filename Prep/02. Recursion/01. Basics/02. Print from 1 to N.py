class Solution:
    def print_1_to_n(self, n: int) -> int:
        if n == 0:
            return
        self.print_1_to_n(n - 1)
        print(n)

    def print_1_to_n_by_tail(self, n: int, k: int = 1) -> int:
        if n == 0:
            return
        print(k)
        self.print_1_to_n_by_tail(n - 1, k + 1)


if __name__ == "__main__":
    s = Solution()
    s.print_1_to_n(10)
    s.print_1_to_n_by_tail(10)

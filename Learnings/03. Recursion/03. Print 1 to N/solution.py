class Solution:
    def print_1_to_n_two_args(self, x: int, n: int) -> None:
        if x > n:
            return
        print(x)
        self.print_1_to_n_two_args(x+1, n)

    def print_1_to_n(self, n: int) -> None:
        if n < 1:
            return
        self.print_1_to_n(n-1)
        print(n)

    def print_n_to_1(self, n: int) -> None:
        if n < 1:
            return
        print(n)
        self.print_1_to_n(n-1)


if __name__ == "__main__":
    obj = Solution()
    print("Print 1 to N (Two arg)")
    obj.print_1_to_n_two_args(1, 4)
    print("-------\nPrint 1 to N (One arg)")
    obj.print_1_to_n(4)
    print("-------\nPrint N to 1")
    obj.print_n_to_1(4)

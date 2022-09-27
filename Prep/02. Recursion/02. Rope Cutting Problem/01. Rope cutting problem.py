class Solution:
    def rope_cutting_problem(self, n: int, a: int, b: int, c: int) -> int:
        if n == 0:
            return 0
        if n <= 0:
            return -1

        res = max(
            self.rope_cutting_problem(n - a, a, b, c),
            self.rope_cutting_problem(n - b, a, b, c),
            self.rope_cutting_problem(n - c, a, b, c),
        )

        if res == -1:
            return -1
        return res + 1


if __name__ == "__main__":
    s = Solution()
    print(s.rope_cutting_problem(5, 2, 5, 1))

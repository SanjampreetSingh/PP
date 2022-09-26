class Solution:
    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    s = Solution()
    print(s.fibonacci(10))

class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def tail_factorial(self, n: int, k: int = 1) -> int:
        if n == 0:
            return k
        return self.tail_factorial(n - 1, n * k)


if __name__ == "__main__":
    s = Solution()
    print(s.factorial(10))
    print(s.tail_factorial(10))

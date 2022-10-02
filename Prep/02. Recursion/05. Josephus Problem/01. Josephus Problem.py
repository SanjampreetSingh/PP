class Solution:
    def josephus(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        return (self.josephus(n - 1, k) + k) % n


if __name__ == "__main__":
    s = Solution()
    print(s.josephus(7, 3))

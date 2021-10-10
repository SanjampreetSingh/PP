class Solution:
    def factorial(self, n: int) -> int:
        # Termination Condition
        if n == 0:
            return 1
        # Recurrence Relation
        else:
            return self.factorial(n-1)*n


if __name__ == "__main__":
    obj = Solution()
    print(obj.factorial(10))

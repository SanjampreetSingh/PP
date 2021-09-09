
class Solution:
    def two_branch(self, n: int):
        print(n)
        # Termination Condition
        if n >= 3:
            return
        # Recurrence Relation
        else:
            self.two_branch(n+1)
            self.two_branch(n+2)


if __name__ == "__main__":
    obj = Solution()
    obj.two_branch(0)

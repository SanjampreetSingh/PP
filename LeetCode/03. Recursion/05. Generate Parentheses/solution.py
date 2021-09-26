from typing import List


class Solution:
    def __init__(self) -> None:
        self.output = []

    def generateParenthesis(self, n: int) -> List[str]:
        s = [""]*(2*n)
        self.balanced_paranthesis(n, 0, 0, 0, s)
        return self.output

    def balanced_paranthesis(self, n: int, l: int, r: int, i: int, s: List[chr]) -> None:
        if i == 2*n:
            self.output.append("".join(s))
            return

        if l == r:
            s[i] = '('
            self.balanced_paranthesis(n, l+1, r, i+1, s)
        elif (l > r):
            if l == n:
                s[i] = ')'
                self.balanced_paranthesis(n, l, r+1, i+1, s)
            else:
                s[i] = '('
                self.balanced_paranthesis(n, l+1, r, i+1, s)
                s[i] = ')'
                self.balanced_paranthesis(n, l, r+1, i+1, s)


if __name__ == "__main__":
    obj = Solution()
    print(obj.generateParenthesis(3))

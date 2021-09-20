from typing import List


class Solution:
    def __init__(self) -> None:
        self.all_combinations = []

    def print_all_combinations(self, temp: List, digits: str, i: int, digitMap: List) -> None:
        if i == len(digits):
            self.all_combinations.append("".join(temp))
            return

        j = 0

        while j < len(digitMap[int(digits[i]) - 2]):
            temp[i] = digitMap[int(digits[i]) - 2][j]
            self.print_all_combinations(
                temp,
                digits,
                i+1,
                digitMap
            )
            j += 1

    def letter_combinations(self, digits: str) -> None:
        n = len(digits)
        if n == 0:
            return

        digitMap = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        temp = [0]*n

        self.print_all_combinations(temp, digits, 0, digitMap)
        return self.all_combinations


if __name__ == "__main__":

    obj = Solution()
    print(obj.letter_combinations("23"))

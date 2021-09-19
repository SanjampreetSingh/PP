from typing import List


class Solution:
    def print_all_combinations(self, temp: str, digits: str, i: int, digitMap: List) -> None:
        if i == len(digits):
            print(temp)
            return

        j = 0
        while j < len(digitMap[int(digits[i]) - 2]):
            self.print_all_combinations(
                temp+digitMap[int(digits[i]) - 2][j],
                digits,
                i+1,
                digitMap
            )
            j += 1

    def letter_combinations(self, digits: str) -> None:
        if len(digits) == 0:
            return

        digitMap = []
        digitMap.append(['a', 'b', 'c'])
        digitMap.append(['d', 'e', 'f'])
        digitMap.append(['g', 'h', 'i'])
        digitMap.append(['j', 'k', 'l'])
        digitMap.append(['m', 'n', 'o'])
        digitMap.append(['p', 'q', 'r', 's'])
        digitMap.append(['t', 'u', 'v'])
        digitMap.append(['w', 'x', 'y', 'z'])

        self.print_all_combinations("", digits, 0, digitMap)


if __name__ == "__main__":

    obj = Solution()
    obj.letter_combinations("23")

class Solution:
    def sum_of_digits(self, number: int) -> int:
        if number <= 9:
            return number
        return self.sum_of_digits(number // 10) + number % 10


if __name__ == "__main__":
    s = Solution()
    print(s.sum_of_digits(9987))

# time complexity is theta d
# space complexity is theta d
# where d is the number of digits in the number

class Solution:
    def count_total_digits_in_a_number(self, number: int) -> int:
        if number <= 9:
            return 1
        return self.count_total_digits_in_a_number(number // 10) + 1


if __name__ == "__main__":
    s = Solution()
    print(s.count_total_digits_in_a_number(99999))

# time complexity is theta d
# space complexity is theta d
# where d is the number of digits in the number

class Solution:
    def sum_of_first_n_natural_numbers(self, number: int) -> int:
        if number == 0:
            return 0
        return self.sum_of_first_n_natural_numbers(number - 1) + number


if __name__ == '__main__':
    s = Solution()
    print(s.sum_of_first_n_natural_numbers(5))

# time complexity is O(n)
# space complexity is O(n)
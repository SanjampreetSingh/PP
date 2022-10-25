class Solution:
    def palindrome(self, n: int) -> bool:
        temp = n
        reverse = 0

        while temp != 0:
            last_digit = temp % 10
            reverse = reverse * 10 + last_digit
            temp = temp // 10

        return reverse == n


if __name__ == "__main__":
    s = Solution()
    print(s.palindrome(12321))

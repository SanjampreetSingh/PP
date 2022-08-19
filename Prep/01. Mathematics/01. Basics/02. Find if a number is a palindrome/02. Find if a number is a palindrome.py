# 02. Find if a number is a palindrome
class Solution:
    def palindrome(self, number: int) -> bool:
        """
        :type number: int
        :rtype: bool
        """
        temp = number
        reverse = 0
        while int(temp) > 0:
            reverse = int((reverse * 10) + (temp % 10))
            temp /= 10

        return reverse == number


if __name__ == "__main__":
    s = Solution()
    print(s.palindrome(123))

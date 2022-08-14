class Solution:
    def by_modulo(self, a):
        if ((a % 2) == 0):
            return "Number is Even"
        else:
            return "Number is Odd"

    def by_bitwise_and(self, a):
        if ((a & 1) == 0):
            return "Number is Even"
        else:
            return "Number is Odd"


if __name__ == '__main__':
    obj = Solution()
    print(obj.by_modulo(2))
    print(obj.by_bitwise_and(30))

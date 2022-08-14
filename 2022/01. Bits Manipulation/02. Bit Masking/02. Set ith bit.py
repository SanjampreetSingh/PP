class Solution:
    def ith_bit(self, number: int, i: int) -> int:
        # k = i - 1
        # mask = 1 << k

        # ith_bit = number | mask

        # return ith_bit
        return self.decimal_to_binary(number | (1 << (i - 1)))

    def decimal_to_binary(self, n):
        return "{0:b}".format(int(n))


if __name__ == "__main__":
    obj = Solution()
    print(obj.ith_bit(11, 4))

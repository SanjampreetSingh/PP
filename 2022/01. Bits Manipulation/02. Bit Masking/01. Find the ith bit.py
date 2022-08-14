class Solution:
    def ith_bit(self, number: int, i: int) -> int:
        # k = i - 1
        # mask = 1 << k

        # and_operation = number & mask

        # ith_bit = and_operation >> k

        # return ith_bit
        return (number & (1 << (i - 1))) >> (i - 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.ith_bit(12, 2))

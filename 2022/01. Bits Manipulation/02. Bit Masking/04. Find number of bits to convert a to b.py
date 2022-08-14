class Solution:
    def number_of_bits(self, num1: int, num2: int) -> int:
        xor = num1 ^ num2
        # xor return difference between num1 and num2
        # n & (n-1) used to compute count
        count = 0
        while xor != 0:
            count += 1
            xor = xor & (xor-1)

        return count


if __name__ == "__main__":
    obj = Solution()
    print(obj.number_of_bits(27, 22))

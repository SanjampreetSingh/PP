class Solution:
    def using_three_variables(self, a, b):
        temp = a
        a = b
        b = temp
        return a, b

    def using_bitwise_xor(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b


if __name__ == "__main__":
    obj = Solution()
    print(obj.using_three_variables(1, 2))
    print(obj.using_bitwise_xor(1, 2))

from typing import List


class Solution:
    def generate_bit_count_of_n_digits(self, n: int) -> List:
        lst = []
        for i in range(2**n):
            b = bin(i)[2:]
            l = len(b)
            b = str(0) * (n - l) + b
            lst.append(b)

        return lst


if __name__ == "__main__":
    obj = Solution()
    digits = obj.generate_bit_count_of_n_digits(3)
    for i in digits:
        print(i)

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

    def print_subsets(self, inputList: List[int], size: int, bitmap: List[int]) -> List[int]:
        for i in bitmap:
            temp = []
            for j in range(size):
                if str(i)[j] == str(1):
                    temp.append(inputList[j])
            print(temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        digits = obj.generate_bit_count_of_n_digits(n)
        if n == 0:
            return
        self.print_subsets(nums, n, digits)


if __name__ == "__main__":

    obj = Solution()
    obj.subsets([1, 2, 3])

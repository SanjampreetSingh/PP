from typing import List


class Solution:
    def print_subsets(self, inputList: List[int], size: int) -> List[int]:
        output = []
        for i in range(2**size):
            temp = []
            b = bin(i)[2:]
            l = len(b)
            b = str(0) * (size - l) + b
            for j in range(size):
                if b[j] == str(1):
                    temp.append(inputList[j])
            output.append(temp)
        return output

    def subsets(self, nums: List) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return
        output = self.print_subsets(nums, n)
        return output


if __name__ == "__main__":

    obj = Solution()
    print(obj.subsets([1, 2, 4]))

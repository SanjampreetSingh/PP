from typing import List


class Solution:
    def __init__(self) -> None:
        self.output = []

    def print_subsets(self, inputList: List, tmp: List, index: int, size: int) -> None:
        if index == len(inputList):
            self.output.append(tmp[:size])
            return

        tmp[size] = inputList[index]
        self.print_subsets(inputList, tmp, index+1, size+1)
        self.print_subsets(inputList, tmp, index+1, size)

    def subsets(self, nums: List) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return
        self.print_subsets(nums, [0]*n, 0, 0)
        return self.output


if __name__ == "__main__":

    obj = Solution()
    print(obj.subsets([1, 2, 4]))

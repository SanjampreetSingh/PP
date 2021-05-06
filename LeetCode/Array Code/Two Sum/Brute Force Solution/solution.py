from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(0, n):
            for j in range(i+1, n):
                if target == nums[i]+nums[j]:
                    return [i, j]

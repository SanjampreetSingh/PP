# [1512] Number of Good Pairs
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = (101)*[0]

        for i in nums:
            count += freq[i]
            freq[i] = freq[i] + 1

        return count

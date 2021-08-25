from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        len_arr = len(height)

        prefix_max = [0]*len_arr
        prefix_max[0] = height[0]
        for i in range(1, len_arr):
            prefix_max[i] = max(prefix_max[i-1], height[i])

        suffix_max = [0]*len_arr
        suffix_max[len_arr-1] = height[len_arr-1]
        for i in range(len_arr-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])

        water_collected = 0
        for i in range(1, len_arr-1):
            deciding_height = min(prefix_max[i-1], suffix_max[i+1])
            if (deciding_height > height[i]):
                water_collected += deciding_height - height[i]

        return water_collected

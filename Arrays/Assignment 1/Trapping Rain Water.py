from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n > 0:
            p_max = [0]*n
            s_max = [0]*n
            amt = 0
            p_max[0] = height[0]
            s_max[n-1] = height[n-1]

            for i in range(1, n):
                p_max[i] = max(p_max[i-1], height[i])

            for i in range(n-2, -1, -1):
                s_max[i] = max(s_max[i+1], height[i])

            for i in range(1, n-1):
                decide_ht = min(p_max[i-1], s_max[i+1])
                if decide_ht <= height[i]:
                    pass
                else:
                    amt += (decide_ht - height[i])

            return amt
        else:
            return 0

"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""

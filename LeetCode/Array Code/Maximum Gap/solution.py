from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        ans, prev = 0, None

        if min_val == max_val:
            return 0

        gap = (max_val - min_val)/(n-1)
        if ((max_val - min_val) % (n-1) != 0):
            gap += 1

        max_arr = [None]*n
        min_arr = [None]*n

        for i in range(n):
            bkt = int((nums[i] - min_val)/gap)
            min_arr[bkt] = nums[i] if min_arr[bkt] is None else\
                min(min_arr[bkt], nums[i])
            max_arr[bkt] = nums[i] if max_arr[bkt] is None else\
                max(max_arr[bkt], nums[i])

        for i in range(n):
            if (min_arr[i] == None):
                continue

            if prev == None:
                prev = max_arr[i]
            else:
                ans = max(ans, (min_arr[i]-prev))
                prev = max_arr[i]

        return ans

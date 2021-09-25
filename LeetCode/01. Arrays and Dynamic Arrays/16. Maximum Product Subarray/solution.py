from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_a = max_a = nums[0]
        ans = max_a

        for i in range(1, n):
            temp_max = max(max_a*nums[i], nums[i], min_a*nums[i])
            min_a = min(min_a*nums[i], nums[i], max_a*nums[i])
            max_a = temp_max
            ans = max(max_a, ans)

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProduct([0,2]))

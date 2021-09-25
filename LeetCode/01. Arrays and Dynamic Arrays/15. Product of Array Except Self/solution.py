from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s_prod = [0]*n
        s_prod[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            s_prod[i] = s_prod[i+1] * nums[i]

        x = nums[0]
        p_prod = 1
        s_prod[0] = s_prod[1]

        for i in range(1, n-1):
            p_prod *= x
            x = nums[i]
            s_prod[i] = p_prod*s_prod[i+1]

        s_prod[n-1] = p_prod * x
        return s_prod


if __name__ == "__main__":
    obj = Solution()
    print(obj.productExceptSelf([4, 3, 2, 1, 2]))

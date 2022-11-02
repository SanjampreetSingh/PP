class Solution:
    def smaller_elements(self, lst: list, x: int) -> list:
        return [i for i in lst if i < x]


class Solution:
    s = Solution()
    print(s.smaller_elements([1, 2, 3, 4, 5, 5], 4))

class Solution:
    # def odd_even(self, lst: list) -> list:
    #     odd = []
    #     even = []
    #     for i in lst:
    #         if i % 2 == 0:
    #             even.append(i)
    #         else:
    #             odd.append(i)

    #     return odd, even

    def odd_even(self, lst: list) -> list:
        odd = [i for i in lst if i % 2 != 0]
        even = [i for i in lst if i % 2 == 0]
        return odd, even


if __name__ == "__main__":
    s = Solution()
    odd, even = s.odd_even([1, 2, 3, 4, 5])
    print("Odd are: " + str(odd))
    print("Even are: " + str(even))

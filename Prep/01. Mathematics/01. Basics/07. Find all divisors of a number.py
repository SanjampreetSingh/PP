class Solution:
    def naive_solution(self, number: int) -> list:
        """
        :type number: int
        :rtype: List[int]
        Time Complexity is O(number)
        """
        i = 1
        res = []
        while i <= number:
            if number % i == 0:
                res.append(i)
            i += 1

        return res

    def efficient_solution(self, number: int) -> list:
        """
        :type number: int
        :rtype: List[int]
        Time Complexity is O(sqrt number)
        """
        res = []
        i = 1
        while i * i <= number:
            if number % i == 0:
                res.append(i)
            i += 1

        while i >= 1:
            if number % i == 0:
                res.append(number // i)
            i -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(15))
    print(s.efficient_solution(100))

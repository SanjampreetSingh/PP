class Solution:
    def naive_solution(self, number: int) -> int:
        fact = 1
        while number != 0:
            fact *= number
            number -= 1

        count = 0
        while fact % 10 == 0:
            count += 1
            fact = fact // 10

        return count

    def efficient_solution(self, number: int) -> int:
        # This solution helps overcome TLE and Space problems
        # Here we look for number of 5's in the factorial's factors and add to count
        # Complexity is O(log number)
        count = 0
        i = 5
        while i < number:
            count += number // i
            i *= 5

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(100))
    print(s.efficient_solution(100))

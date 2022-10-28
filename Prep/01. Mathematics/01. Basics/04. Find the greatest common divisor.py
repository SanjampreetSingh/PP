class Solution:
    def naive_solution(self, num1: int, num2: int) -> int:
        # In case the solution is 1 that's when we don't have a common divisor,
        # the time complexity of the solution would be O(min(num1, num2))
        min_val = min(num1, num2)
        while min_val > 0:
            if num1 % min_val == 0 and num2 % min_val == 0:
                break
            min_val -= 1

        return min_val

    def euclidean_solution(self, num1: int, num2: int) -> int:
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1

        return num1

    def euclidean_solution_optimized(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return num1
        return self.euclidean_solution_optimized(num2, num1%num2)


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(100, 200))
    print(s.euclidean_solution(10, 15))
    print(s.euclidean_solution_optimized(9, 13))

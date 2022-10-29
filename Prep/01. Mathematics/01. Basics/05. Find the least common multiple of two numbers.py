class Solution:
    def naive_solution(self, num1: int, num2: int) -> int:
        max_val = max(num1, num2)
        while True:
            if max_val % num1 == 0 and max_val % num2 == 0:
                return max_val
            max_val += 1

    def gcd(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return num1
        return self.gcd(num2, num1 % num2)

    def optimized_solution(self, num1: int, num2: int) -> int:
        # (num1 * num2) = lcm(num1, num2) * gcd(num1, num2)
        return (num1 * num2) // self.gcd(num1, num2)


if __name__ == "__main__":
    s = Solution()
    print(s.naive_solution(8, 6))
    print(s.optimized_solution(8, 6))

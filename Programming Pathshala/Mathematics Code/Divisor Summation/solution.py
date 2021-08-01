class Solution:
    def sum_of_proper_divisors(self, n: int) -> int:
        sum = 0
        i = 1

        if n == 1:
            return 0

        while i*i <= n:
            if n % i == 0:
                sum += i
                n_by_i = n//i
                if n_by_i < n and n_by_i != i:
                    sum += n_by_i
            i += 1
        return sum


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    for _ in range(T):
        print(obj.sum_of_proper_divisors(int(input())))

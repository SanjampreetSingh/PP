from typing import List, Set


class Solution:
    def sieve(self, upper_limit: int = 10**6) -> Set:
        itr = 2
        primes = [True]*(upper_limit+1)
        primes[1] = False
        square_of_primes = set()

        while itr*itr <= upper_limit+1:
            if primes[itr]:
                for itr_1 in range(itr*itr, upper_limit, itr):
                    if primes[itr_1]:
                        primes[itr_1] = False
            itr += 1

        for val in range(2, upper_limit+1):
            if primes[val]:
                square_of_primes.add(val*val)

        return square_of_primes

    def sum_three_prime_numbers(self, input_list: List, square_of_primes: Set) -> int:
        sum_t_primes = 0

        for num in input_list:
            if num in square_of_primes:
                sum_t_primes += num

        return sum_t_primes


if __name__ == "__main__":
    test = int(input())
    object = Solution()
    square_of_primes = object.sieve()
    for _ in range(test):
        no_of_inputs = int(input())
        print(object.sum_three_prime_numbers(
            list(map(int, input().strip().split()))[:no_of_inputs], square_of_primes))

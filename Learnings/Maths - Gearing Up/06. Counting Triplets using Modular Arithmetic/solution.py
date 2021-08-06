
from typing import List


class Solution:
    def count_triplets(self, remainder_arr: List, divisor: int) -> int:
        count = 0
        i = 0
        k = 0
        while i < divisor:
            j = i
            while j < divisor:
                remainder_two_pair = (i+j) % divisor

                if (remainder_two_pair) == 0:
                    k = 0
                else:
                    k = (divisor - remainder_two_pair)
                if k > j:
                    j += 1
                    continue

                if i == j and j == k:
                    count += ((remainder_arr[i] * (remainder_arr[i] - 1)
                               * (remainder_arr[i] - 2)) // 6)
                elif i == j:
                    count += (((remainder_arr[i]) * (remainder_arr[i]-1)
                               ) // 2) * (remainder_arr[k])
                elif i == k:
                    count += (((remainder_arr[i]) * (remainder_arr[i]-1)
                               ) // 2) * (remainder_arr[j])
                elif k == j:
                    count += (((remainder_arr[j]) * (remainder_arr[j]-1)
                               ) // 2) * (remainder_arr[i])
                else:
                    count += (remainder_arr[i] *
                              remainder_arr[j] * remainder_arr[k])
                j += 1
            i += 1

        return count

    def get_remainders(self, divisor: int, input_arr: List) -> List:
        remainders = [0]*divisor

        for i in input_arr:
            remainders[i % divisor] += 1

        return remainders


if __name__ == "__main__":
    divisor = 8
    input_arr = [0, 8, 1, 16, 12, 13, 53, 218]
    obj = Solution()
    remainders = obj.get_remainders(divisor, input_arr)
    print(obj.count_triplets(remainders, divisor))

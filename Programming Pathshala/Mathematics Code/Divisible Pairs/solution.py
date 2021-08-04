from typing import List


class Solution:
    def divisible_pairs(self, four_count: List) -> int:
        ans = 0

        ans += (four_count[0] * (four_count[0]-1))//2
        ans += (four_count[1]*four_count[3])
        ans += (four_count[2] * (four_count[2]-1))//2

        return ans

    def pair_four(self, n: int, arr: List) -> List:
        four_count = [0]*4

        for i in range(n):
            four_count[arr[i] % 4] += 1

        return four_count


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    for _ in range(T):
        N = int(input())
        four_count = obj.pair_four(
            N, list(map(int, input().strip().split()))[:N])
        print(obj.divisible_pairs(four_count))

from typing import List


class Solution:
    def pascal_triangle(self) -> List:
        pascal = [[0 for i in range(0, 62)]for j in range(0, 62)]
        pascal[0][0] = 1

        for i in range(1, 62):
            for j in range(62):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

        return pascal

    def making_teams(self, n: int, m: int, x: int, pascal: List) -> int:
        ans = 0
        ans += pascal[n+m][x]
        if (x <= m):
            ans -= pascal[n][0] * pascal[m][x]
        if (x-1 <= m):
            ans -= n * pascal[m][x-1]
        if (x-2 <= m):
            ans -= pascal[n][2] * pascal[m][x-2]
        if (x-3 <= m):
            ans -= pascal[n][3] * pascal[m][x-3]
        if (x <= n):
            ans -= pascal[n][x] * pascal[m][0]
        return ans


if __name__ == "__main__":
    T = int(input())
    obj = Solution()
    pas = obj.pascal_triangle()
    for _ in range(T):
        n, m, x = map(int, input().split())
        print(obj.making_teams(n, m, x, pas))

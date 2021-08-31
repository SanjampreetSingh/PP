from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        arr = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(1, m):
                mat[i][j] = mat[i][j] + mat[i][j-1]

        for i in range(1, n):
            for j in range(m):
                mat[i][j] = mat[i][j] + mat[i-1][j]

        for i in range(n):
            for j in range(m):

                r1 = 0 if i-k < 0 else i-k
                c1 = 0 if j-k < 0 else j-k
                r2 = n - 1 if i+k >= n else i+k
                c2 = m - 1 if j+k >= m else j+k

                current_region_sum = mat[r2][c2]
                left_region_sum = mat[r2][c1 - 1] if c1 != 0 else 0
                top_region_sum = mat[r1 - 1][c2] if r1 != 0 else 0
                common_region = mat[r1 - 1][c1 - 1] \
                    if r1 != 0 and c1 != 0 else 0
                arr[i][j] = current_region_sum - top_region_sum - \
                    left_region_sum + common_region

        return arr

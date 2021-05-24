from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        if (m == 0 or n == 0):
            return

        # make prefix sums for rows
        for row in range(m):
            for col in range(1, n):
                matrix[row][col] = matrix[row][col - 1] + matrix[row][col]

        for row in range(1, m):
            for col in range(n):
                matrix[row][col] = matrix[row][col] + matrix[row - 1][col]

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current_region_sum = self.matrix[row2][col2]
        left_region_sum = self.matrix[row2][col1 - 1] if col1 != 0 else 0
        top_region_sum = self.matrix[row1 - 1][col2] if row1 != 0 else 0
        common_region = self.matrix[row1 - 1][col1 - 1] \
            if row1 != 0 and col1 != 0 else 0

        return current_region_sum - top_region_sum - left_region_sum + common_region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

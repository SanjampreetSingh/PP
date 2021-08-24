class Solution:
    def pascal_triangle(self):
        pascal = [[0 for i in range(0, 1001)]for j in range(0, 1001)]
        pascal[0][0] = 1

        for i in range(1, 1001):
            for j in range(1001):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

        return pascal


if __name__ == "__main__":
    n = 10
    r = 6

    obj = Solution()
    pas = obj.pascal_triangle()
    print(pas[n][r])

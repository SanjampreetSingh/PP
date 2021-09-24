
class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def find_max(self, i: int, j: int) -> int:
        if i == j:
            return arr[i]

        m = int((i+j)/2)

        m1 = self.find_max(i, m)
        m2 = self.find_max(m+1, j)

        return max(m1, m2)


if __name__ == "__main__":
    arr = [7, 1, 4, 3, 2, 6, 5]
    n = len(arr)
    obj = Solution(arr)
    print(obj.find_max(0, n-1))

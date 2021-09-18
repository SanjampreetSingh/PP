count = 0


class Solution:
    def __init__(self, m, n) -> None:
        self.m = m
        self.n = n

    def count_paths(self, i: int, j: int) -> int:
        if i == self.m-1 or j == self.n-1:
            return 1

        return self.count_paths(i, j+1) + self.count_paths(i+1, j)

    def count_paths_from_destination(self, i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 1

        return self.count_paths_from_destination(i, j-1) + self.count_paths_from_destination(i-1, j)

    def count_paths_void(self, i: int, j: int) -> None:
        """
        Using Global variable to update the value in termination condition
        """
        global count
        if i == self.m-1 or j == self.n-1:
            count += 1
            return

        self.count_paths_void(i, j+1)
        self.count_paths_void(i+1, j)


if __name__ == "__main__":
    obj = Solution(3, 3)
    print("Int based method: " + str(obj.count_paths(0, 0)))
    print("Int based method in Bottom to Top approach: " + str(obj.count_paths_from_destination(2, 2)))
    obj.count_paths_void(0, 0)
    print("Void based method: " + str(count))

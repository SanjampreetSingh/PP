class Solution:
    def tower_of_hanoi(self, n, fromm, to, aux):
        if n == 0:
            return
        self.tower_of_hanoi(n - 1, fromm, aux, to)
        print("move disk " + str(n) + " from rod " + str(fromm) + " to rod " + str(to))
        self.tower_of_hanoi(n - 1, aux, to, fromm)
        return pow(2, n) - 1


if __name__ == "__main__":
    s = Solution()
    print("Number of steps = " + str(s.tower_of_hanoi(3, 1, 2, 3)))

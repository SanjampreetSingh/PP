class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0/self.myPow(x, (-1*n))
        if n == 0:
            return 1

        val = self.myPow(x, n//2)

        if n % 2 == 0:
            val *= val
        else:
            val *= val*x

        return val


if __name__ == "__main__":

    obj = Solution()
    print(obj.subsets(2, 4))

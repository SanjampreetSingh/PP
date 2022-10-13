class Solution:
    def check_duplicate_in_array(self, array: list) -> str:
        size = 1
        for i in range(1, len(array)):
            if array[i] != array[size - 1]:
                array[size] = array[i]
                size += 1

        for i in range(size, len(array)):
            array[i] = "-"

        return f"Size of array: {size}. \n Array: {array}"


if __name__ == "__main__":
    s = Solution()
    print(s.check_duplicate_in_array([10, 10, 20, 20, 30, 30, 30]))

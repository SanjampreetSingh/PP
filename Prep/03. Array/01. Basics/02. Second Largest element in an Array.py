class Solution:
    def second_largest_element_in_an_array(self, array: list) -> int:
        res = -1
        largest_element = 0
        for i in range(1, len(array)):
            if array[i] > array[largest_element]:
                res = largest_element
                largest_element = i
            elif array[i] != array[largest_element]:
                if res == -1 or array[i] > array[res]:
                    res = i

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.second_largest_element_in_an_array([-10,-10,-10]))
class Solution:
    def largest_element_in_array(self, arr) -> int:
        temp = 0
        for i in range(1,len(arr)):
            if arr[temp] < arr[i]:
                temp = i

        return temp

if __name__ == "__main__":
    s = Solution()
    print(s.largest_element_in_array([5, 8, 20, 10]))

class Solution:
    def binary_search(self, arr: list, element: int) -> int:
        low = 0
        high = len(arr)

        while low <= high:
            mid = (high + low)//2
            if element == arr[mid]:
                return mid
            elif element > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1



if __name__ == '__main__':
    s = Solution()
    print(s.binary_search([10,20,30,40,50,60,70,80], 30))
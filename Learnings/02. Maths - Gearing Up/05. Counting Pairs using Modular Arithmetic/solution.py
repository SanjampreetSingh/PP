from typing import List


class Solution:
    def counting_pairs(self, k: int, count_arr: List) -> int:
        count = 0

        # Add count for 0 remainder value
        count += (count_arr[0]*(count_arr[0]-1))//2
        # add count for pairs i, k-i
        for i in range(1, (k//2)):
            count += (count_arr[i]*count_arr[k-i])

        # check if k is odd or even
        if k % 2 == 0:
            # Add central remainder count
            count += (count_arr[k//2]*(count_arr[k//2]-1))//2
        else:
            # add count for pairs i, k+i
            count += count_arr[k//2]*count_arr[(k//2)+i]

        return count

    def count_remainders(self, arr_input: List, k: int) -> List:
        count_arr = [0]*k

        for val in arr_input:
            count_arr[val % k] += 1

        return count_arr


if __name__ == "__main__":
    arr_input = [2, 2, 1, 7, 5, 3]
    k = 4
    obj = Solution()
    count_arr = obj.count_remainders(arr_input, k)
    print(obj.counting_pairs(k, count_arr))

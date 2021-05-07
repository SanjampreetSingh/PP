from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        person = 0
        for i in range(n):
            sum_i = sum(accounts[i])
            sum_person = sum(accounts[person])
            if sum_i > sum_person:
                person = i

        return sum(accounts[person])

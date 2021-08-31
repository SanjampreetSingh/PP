from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        n = len(items)
        dict_key = {"type": 0, "color": 1, "name": 2}

        for i in range(n):
            if ruleValue == items[i][dict_key[ruleKey]]:
                count += 1
        return count

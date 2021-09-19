import math
from typing import Collection, List


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        gcd = 0
        # Find frequency of each card number
        freq = Collection.Counter(deck)

        # Calculate GCD of freq dictionary 
        for (key, value) in freq.items():
            if gcd == 0:
                gcd = value
            else:
                gcd = math.gcd(gcd, value)

        if gcd == 1:
            return False
        return True

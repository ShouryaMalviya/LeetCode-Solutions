from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        # Count the frequency of each card
        frequencies = Counter(deck).values()
        
        # Find the GCD of all frequencies and check if it's >= 2
        return math.gcd(*frequencies) >= 2
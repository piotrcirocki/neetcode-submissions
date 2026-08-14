import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_diff = None
        min_val = prices[0]

        for ix, val in enumerate(prices):
            if ix > 0:
                if min_val > prices[ix]:
                    min_val = prices[ix]
                temp_diff = prices[ix] - min_val
                if temp_diff > 0 and current_diff is None:
                    current_diff = temp_diff
                elif temp_diff > 0 and current_diff < temp_diff:
                    current_diff = temp_diff
                else:
                    pass

        if current_diff is None:
            return 0
        else:
            return current_diff
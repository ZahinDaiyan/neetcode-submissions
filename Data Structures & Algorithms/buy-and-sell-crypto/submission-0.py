class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        mx_profit = 0
        for p in prices:
            if p < minp:
                minp = p
            
            profit = p - minp

            if profit > mx_profit:
                mx_profit = profit
        return mx_profit
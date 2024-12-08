'''
Best Time to Buy and Sell Stock
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1
    max_profit = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(prices[r]-prices[l], max_profit)
        else:
            l = r
        r += 1 
    
    return max_profit
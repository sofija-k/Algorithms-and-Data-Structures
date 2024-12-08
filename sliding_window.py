from typing import List
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

'''
Longest Substring Without Repeating Characters
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    substring = {}
    length = 0
    
    for r in range(len(s)):
        if s[r] in substring:
            l = max(l, substring[s[r]] + 1)
            
        substring[s[r]] = r
        length = max(length, r-l+1)
        print(substring, length)

    return length
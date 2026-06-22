class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        maximum = 0
        for i in prices:
            if i< minimum:
                minimum = i
            profit = i - minimum
            if profit > maximum:
                maximum = profit
       
        return maximum
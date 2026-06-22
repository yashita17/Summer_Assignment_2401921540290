class Solution(object):
    def sortedSquares(self, nums):
        num = list(map(lambda i: i*i, nums))
        num.sort()
        return num
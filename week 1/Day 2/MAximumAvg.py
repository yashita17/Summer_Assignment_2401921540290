class Solution(object):
    def findMaxAverage(self, nums, k):
        sum = 0
        for i in range(k):
            sum = sum + nums[i]
        maximum = sum
        for j in range(k, len(nums)):
            sum = sum - nums[j-k] + nums[j]
            if sum > maximum:
                maximum = sum
        return maximum / float(k)
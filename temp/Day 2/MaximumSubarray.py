class Solution(object):
    def maxSubArray(self, nums):
        maximum = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maximum = max(maximum, current)
        return maximum
    
    #Another solution by brute force
    def subarray(nums):
        m = nums[0]
        s = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s = s + nums[j]
                if s> m:
                    m = s
        return m
    


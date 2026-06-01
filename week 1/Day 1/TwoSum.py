class Solution(object):
    def TwoSum(self, nums, target):
        #bruteforce approach
        #time complexity O(n square)
        #space complexity O(1)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

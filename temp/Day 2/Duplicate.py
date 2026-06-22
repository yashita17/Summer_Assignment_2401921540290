class Solution(object):
    def containsDuplicate(self, nums):
        unique = set() #have an empty set
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
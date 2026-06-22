class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dict = {}
        for i in nums2:
            while stack and i > stack[-1]:
                dict[stack[-1]] = i
                stack.pop()

            stack.append(i)
        while stack:
            dict[stack[-1]] = -1
            stack.pop()
        ans = []
        for i in nums1:
            ans.append(dict[i])
        return ans
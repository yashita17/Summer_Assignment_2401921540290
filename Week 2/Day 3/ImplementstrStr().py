class Solution(object):
    def strStr(self, haystack, needle):
        k = len(needle)
        l = len(haystack)
        left = 0
        right = k
        for i in range(l-k +1):
            if needle == haystack[left:right]:
                return left
            else:
                left +=1
                right+=1
        return -1
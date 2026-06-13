class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        j = 0
        for i in t :
            if j <len(s) and i == s[j]:
                j +=1
        if j == len(s):
            return True
        return False
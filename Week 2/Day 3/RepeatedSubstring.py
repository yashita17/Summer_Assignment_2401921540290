class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range (1, n//2 +1):
            if n % 1 == 0:
                new = s[:i]
                if new *(n//i) == s:
                    return True
        return False
        
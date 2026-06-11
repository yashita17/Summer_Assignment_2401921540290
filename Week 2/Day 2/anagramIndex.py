class Solution(object):
    def findAnagrams(self, s, p):
        l = len(p)
        m = len(s)
        arr = []
        c1 = {}
        c2 = {}
        for ch in p:
            c1[ch] = c1.get(ch,0) +1
        for ch in s[:l]:
            c2[ch] = c2.get(ch, 0) +1
        if c1 == c2:
            arr.append(0)
        left = 0
        for right in range(l,m):
            c2[s[right]] = c2.get(s[right], 0)+1
            c2[s[left]] -=1
            if c2[s[left]] == 0:
                del c2[s[left]]
            left +=1
            if c1 == c2:
                arr.append(left)
        return arr
        
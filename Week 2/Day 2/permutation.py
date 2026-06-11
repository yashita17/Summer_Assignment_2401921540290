class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)
        m = len(s2)
        count_s1 = {}
        count_s2 = {}
        for ch in s1:
            count_s1[ch] = count_s1.get(ch, 0) +1
        for ch in s2[:k]:
            count_s2[ch] = count_s2.get(ch,0) +1
        if count_s2 == count_s1:
                return True
        left = 0
        for right in range (k,m) :
            count_s2[s2[right]] = count_s2.get(s2[right], 0) +1
            count_s2[s2[left]] -=1
            if count_s2[s2[left]]== 0:
                del count_s2[s2[left]]
            left +=1
            if count_s2 == count_s1:
                return True
        return False 
        
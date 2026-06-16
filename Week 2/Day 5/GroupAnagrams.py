class Solution(object):
    def groupAnagrams(self, strs):
        d= {}
        for words in strs:
            freq = [0] * 26
            for ch in words:
                i = ord(ch) - ord("a")
                freq[i] +=1
            key = tuple(freq)
            if key not in d:
                d[key] = []
            d[key].append(words)
        return list(d.values())

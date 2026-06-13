class Solution(object):
    def reverseWords(self, s):
        result =[]
        for word in s.split():
            word = list(word)
            left = 0
            right = len(word)-1
            while left < right:
                word[left],word[right] = word[right],word[left]
                left +=1
                right-=1
            result.append("".join(word))
        return " ".join(result)
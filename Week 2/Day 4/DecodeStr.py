class Solution(object):
    def decodeString(self, s):
        str1 = ""
        stack =[]
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((str1, num))
                str1 =""
                num = 0
            elif ch == "]":
                str2, num2 = stack.pop()
                str1 = str2 + str1*num2
            else:
                str1 += ch
        return str1
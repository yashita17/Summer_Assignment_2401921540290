class Solution(object):
    def compress(self, chars):
        write = 0
        start = 0
        for right in range(len(chars)+1):
            if right == len(chars) or chars[start] != chars[right]:
                chars[write] = chars[start]
                write +=1
                count = right - start
                if count > 1:
                    for i in str(count):
                        chars[write] = i
                        write += 1
                start = right
        return write
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i]> temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)

        return ans
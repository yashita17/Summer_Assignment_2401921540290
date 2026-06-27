class Solution(object):
    def maxPathSum(self, root):
        self.Total = float('-inf')
        def AddPath(node):
            if not node:
                return 0
            left = max(0, AddPath(node.left))
            right = max(0, AddPath(node.right))

            current = node.val + left + right

            self.Total = max(self.Total, current)

            return node.val + max(left, right)
        
        AddPath(root)

        return self.Total
class Solution(object):
    def isValidBST(self, root):
        def traverse(node, low, high):
            if node == None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return(traverse(node.left, low, node.val) and traverse(node.right, node.val, high))
        
        return traverse(root, float('-inf'), float('inf'))
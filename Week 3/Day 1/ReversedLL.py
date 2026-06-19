class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr :
            NextNode = curr.next
            curr.next = prev
            prev = curr
            curr = NextNode
        return prev

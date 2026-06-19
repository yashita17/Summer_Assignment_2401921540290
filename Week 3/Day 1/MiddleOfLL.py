class Solution(object):
    def middleNode(self, head):
        p  = head
        q = head
        while p != None and p.next != None :
            p = p.next.next
            q = q.next
        return q
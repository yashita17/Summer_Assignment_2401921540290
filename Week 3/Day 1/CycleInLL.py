class Solution(object):
    def hasCycle(self, head):
        p1 = head
        p2 = head
        while p1 != None and p1.next != None:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False
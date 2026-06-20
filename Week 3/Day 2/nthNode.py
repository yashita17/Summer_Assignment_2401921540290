class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l1 = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        curr2 = dummy
        while curr.next:
            curr = curr.next
            l1 +=1
        l2 = l1 - n
        while l2 != 0:
            curr2 = curr2.next
            l2 -=1
        curr2.next = curr2.next.next
        return dummy.next
    

# SECOND SOLUTION USING TWO POINTER
# BOTH HAVE SAME COMPLEXITIES
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range (n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

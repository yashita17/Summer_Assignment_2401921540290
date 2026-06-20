class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        prev = None
        while curr != None:
            NextNode =  curr.next
            curr.next = prev
            prev = curr
            curr = NextNode
        left = head
        right = prev
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
                
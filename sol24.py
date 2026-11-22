class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):

    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head

        current = dummy


        while current.next and current.next.next:

            slow = current.next
            fast = current.next.next

            slow.next = fast.next
            fast.next = slow
            current.next = fast

            current = slow


        return dummy.next

    
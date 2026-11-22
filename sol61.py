class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):

    def rotateRight(self, head, k):

        if head is None or head.next is None:
            return head

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        k = k % length

        dummy = ListNode(0)
        dummy.next = head

        for i in range(k):

            fast = dummy

            while fast.next.next:
                fast = fast.next

            last = fast.next

            fast.next = None

            last.next = dummy.next
            dummy.next = last

        return dummy.next
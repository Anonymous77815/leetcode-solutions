class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while True:

            # Find kth node
            fast = current

            for i in range(k):
                fast = fast.next

                if fast == None:
                    return dummy.next

            # First node of current group
            slow = current.next

            # Save node after kth node
            next_group = fast.next

            # Reverse k nodes
            prev = next_group
            curr = slow

            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Connect previous part to reversed group
            current.next = fast

            # slow is now the last node of reversed group
            current = slow
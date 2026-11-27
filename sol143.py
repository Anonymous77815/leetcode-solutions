class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):


        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half

        while curr:

            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        second_half = prev
        first_half = head

        current1 = first_half
        current2 = second_half

        while current1 and current2:

            temp1 = current1.next
            temp2 = current2.next
            current1.next = current2
            current2.next = temp1

            current1 = temp1
            current2 = temp2


        return head
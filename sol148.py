class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def sortList(self, head):

        current = head
        l = 0


        while current:
            l = l + 1
            current = current.next


        if head is None or head.next is None:
            return head


        mid = l // 2

        current_1 = head

        for i in range(mid - 1):
            current_1 = current_1.next

        current_2 = current_1.next
        current_1.next = None

        left = head
        right = current_2

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def merge(self, left, right):

        head = ListNode(0)
        current = head

        while left and right:

            if left.val < right.val:
                current.next = left
                left = left.next
                current = current.next

            else:
                current.next = right
                right = right.next
                current = current.next


        while left :
            current.next = left
            left = left.next
            current = current.next

        while right:
            current.next = right
            right = right.next
            current = current.next


        return head.next
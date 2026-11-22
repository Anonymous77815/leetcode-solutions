class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current:

            nextNode = current.next

            prev = dummy

            while prev.next and prev.next.val<current.val:
                prev = prev.next


            current.next = prev.next
            prev.next = current

            current = nextNode


        return dummy.next
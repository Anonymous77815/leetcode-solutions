class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy.next
        fast = slow.next if slow else None

        while fast:

            if slow.val == fast.val:
                slow.next = fast.next
                
            else:
                slow = fast


            fast = fast.next


        return dummy.next
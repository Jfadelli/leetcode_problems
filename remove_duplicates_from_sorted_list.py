
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: ListNode):
    while head:
        curr_val, next_val = head.val, head.next.val
        if curr_val < next_val:
            break
        if curr_val == next_val:
            head = head.next  
    return head


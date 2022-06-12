from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        result = ListNode()
        tail = result

        while True:
            if list1.val <= list2.val:
                tail.val = list1.val
                list1 = list1.next
            else:
                tail.val = list2.val
                list2 = list2.next

            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break
            else:
                tail.next = ListNode()
                tail = tail.next

        return result

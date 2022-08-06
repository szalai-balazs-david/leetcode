from typing import Optional
from Utilities.TreeNode import TreeNode
from Utilities.ListNode import ListNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        if head.next.next is None:
            return TreeNode(head.next.val, TreeNode(head.val))
        if head.next.next.next is None:
            return TreeNode(head.next.val, TreeNode(head.val), TreeNode(head.next.next.val))
        right = head
        mid = head
        prev = mid
        while right is not None and right.next is not None:
            right = right.next.next
            prev = mid
            mid = mid.next
        prev.next = None

        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))

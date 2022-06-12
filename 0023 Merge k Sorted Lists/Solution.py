from typing import Optional
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        q = PriorityQueue()
        root = ListNode(0)
        current = root

        for l in lists:
            if l:
                q.put(Wrapper(l))

        while not q.empty():
            node = q.get().node
            current.next = node
            current = current.next
            if node.next:
                q.put(Wrapper(node.next))

        return root.next

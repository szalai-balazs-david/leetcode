from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeNode2List(node: TreeNode) -> list[int]:
    result = []
    current = [node]
    next = []

    while True:
        for c in current:
            if not c:
                result.append(None)
            else:
                result.append(c.val)
                next.append(c.left)
                next.append(c.right)
        done = True
        for n in next:
            if n is not None:
                done = False
                break
        if done:
            break
        current = next
        next = []

    return result

from collections import deque
from typing import Optional
from Utilities.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        def addValues(node: TreeNode, value: int) -> int:
            if node is None:
                return value
            if node.left is not None:
                value = addValues(node.left, value)
            node.val = value
            value += 1
            if node.right is not None:
                value = addValues(node.right, value)
            return value

        def clone(node: TreeNode) -> Optional[TreeNode]:
            if node is None:
                return None
            root = TreeNode()
            q = deque()
            q.append((node, root))
            while q:
                (node, current) = q.pop()
                if node.left is not None:
                    current.left = TreeNode()
                    q.append((node.left, current.left))
                if node.right is not None:
                    current.right = TreeNode()
                    q.append((node.right, current.right))
            return root

        def generateStructure(num: int) -> list[Optional[TreeNode]]:
            if num == 0:
                return [None]
            if num == 1:
                return [TreeNode(0)]
            if num == 2:
                return [TreeNode(0, None, TreeNode(0)), TreeNode(0, TreeNode(0), None)]

            results = []
            for i in range(num):
                lefts = self.generateTrees(i)
                rights = self.generateTrees(num - i - 1)
                for left in lefts:
                    for right in rights:
                        # Optimalization option: Reduce cloning by using the original once
                        results.append(TreeNode(0, clone(left), clone(right)))
            return results

        trees = generateStructure(n)
        for tree in trees:
            addValues(tree, 1)
        return trees

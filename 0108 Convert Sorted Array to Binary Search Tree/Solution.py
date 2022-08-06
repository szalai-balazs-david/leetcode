from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def divideAndConquer(left: int, right: int):
            if left > right:
                return None
            mid = (left + right + 1) // 2
            return TreeNode(nums[mid], divideAndConquer(left, mid-1), divideAndConquer(mid + 1, right))

        return divideAndConquer(0, len(nums) - 1)

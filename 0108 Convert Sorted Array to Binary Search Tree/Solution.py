from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if nums is None:
            return None
        length = len(nums)
        match length:
            case 0:
                return None
            case 1:
                return TreeNode(nums[0])
            case 2:
                return TreeNode(nums[1], TreeNode(nums[0]))
            case 3:
                return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))
        mid = length // 2

        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root_val=max(nums)
        k=nums.index(root_val)
        root=TreeNode(root_val)
        root.left=self.constructMaximumBinaryTree(nums[:k])
        root.right=self.constructMaximumBinaryTree(nums[k+1:])
        return root
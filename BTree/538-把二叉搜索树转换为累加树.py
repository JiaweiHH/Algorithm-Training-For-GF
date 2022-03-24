# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#反中序递归
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.total=0
        def convert(root):
            if root:
                convert(root.right)
                self.total+=root.val
                root.val=self.total
                convert(root.left)
        convert(root)
        return root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        L = root.left
        root.left=root.right
        root.right=L
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



#不存在中间L的递归写法，直接交换，更加快，时间空间复杂度O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.right,root.left=left,right
        return root

#没有想出迭代的方法
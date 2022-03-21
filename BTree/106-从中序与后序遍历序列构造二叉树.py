# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root=TreeNode(postorder[-1])
        k=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[0:k],postorder[0:k])
        root.right=self.buildTree(inorder[k+1:len(postorder)],postorder[k:len(postorder)-1])
        return root

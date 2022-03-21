# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)
        k=inorder.index(root_val)
        root.left=self.buildTree(preorder[1:k+1],inorder[:k])
        root.right=self.buildTree(preorder[k+1:],inorder[k+1:])
        return root

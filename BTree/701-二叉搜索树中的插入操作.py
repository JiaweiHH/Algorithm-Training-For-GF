# Definition for a binary tree node.
#递归
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val)
        return root
#递归优化
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        newNode=TreeNode(val)
        if not root:
            return newNode
        if not root.left and root.val>val:
            root.left=newNode
        if not root.right and root.val<val:
            root.right=newNode
        if root.val<val:
            self.insertIntoBST(root.right,val)
        if root.val>val:
            self.insertIntoBST(root.left,val)
        return root
#迭代
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        cur=root
        parent=None
        while cur:
            if cur.val>val:
                parent=cur
                cur=cur.left
            else:
                parent=cur
                cur=cur.right
        if parent.val>val:
            parent.left=TreeNode(val)
        if parent.val<val:
            parent.right=TreeNode(val)
        return root


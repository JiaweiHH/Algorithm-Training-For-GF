# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己写的递归
from collections import deque


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        def search(root,val):
            if not root:
                return 
            if root.val==val:
                return root
            if root.val<val:
                return search(root.right,val)
            elif root.val>val:
                return search(root.left,val)
        root=search(root,val)
        return root

#更加简单的递归写法
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==val:
            return root
        return self.searchBST(root.left if root.val>val else root.right,val)

#自己写的迭代
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if node.val==val:
                return node
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
#更加简单的迭代
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        while root:
            if root.val==val:
                return root
            root=root.left if root.val>val else root.right
        return None
            
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#递归形式
from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def Symmetric(p,q):#任意2个兄弟节点
            if not q and not p:
                return True
            if not q or not p:
                return False
            return q.val==p.val and Symmetric(p.left,q.right) and Symmetric(p.right,q.left)
        return Symmetric(root,root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#队列形式
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue=deque([root])
        queue.append(root)
        while queue:
            p=queue.popleft()
            q=queue.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val!=q.val:
                return False     
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        leafNode=lambda root:not root.left and not root.right
        if not root:
            return False
        queue=deque([root])
        valuequeue=deque([root.val])
        while queue:
            k=len(queue)
            for i in range(k):
                node=queue.popleft()
                value=valuequeue.popleft()
                if value==targetSum and leafNode(node):
                    return True
                if node.left:
                    queue.append(node.left)
                    valuequeue.append(value+node.left.val)
                if node.right:
                    queue.append(node.right)
                    valuequeue.append(value+node.right.val)
        return False
#递归
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum==root.val
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
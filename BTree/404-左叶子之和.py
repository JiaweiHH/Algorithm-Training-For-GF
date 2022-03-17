# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#广度搜索
from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        sum=0
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    sum+=node.left.val
            if node.right:
                queue.append(node.right)
        return sum

#深度搜索
#递归这个方法没有用脑子！之后再做一遍！！！
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        isLeafNode=lambda root:not root.left and not root.right
        def dfs(root):
            result=0
            if root.left:
                result+=root.left.val if isLeafNode(root.left) else dfs(root.left)
            if root.right:
                result+=dfs(root.right)
            return result
        return dfs(root) if root else 0
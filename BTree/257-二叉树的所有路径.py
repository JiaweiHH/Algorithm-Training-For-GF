# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#迭代
from collections import deque
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result=[]
        nodequeue=deque([root])
        valuequeue=deque([str(root.val)])
        while nodequeue:
            node=nodequeue.popleft()
            value=valuequeue.popleft()
            if not node.left and not node.right:
                result.append(value)
            else:
                if node.left:
                    nodequeue.append(node.left)
                    valuequeue.append(value+'->'+str(node.left.val))
                if node.right:
                    nodequeue.append(node.right)
                    valuequeue.append(value+'->'+str(node.right.val))
        return result
                
#递归
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths=[]
        if not root:
            return paths
        def treePaths(root,path):
            if not root:
                return 
            path+=str(root.val)
            if not root.right and not root.left:
                paths.append(path)
            else:
                path+='->'
                treePaths(root.left,path)
                treePaths(root.right,path)
        treePaths(root,'')
        return paths
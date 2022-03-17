# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#遍历
from collections import deque
from operator import le
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue=deque([root])
        k=0
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                k+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return k
#递归
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        return left+right+1


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=root.left
        right=root.right
        leftheight=0
        rightheight=0
        while left:
            left=left.left
            leftheight+1
        while right:
            right=right.right
            rightheight+=1
        if rightheight==leftheight:#判断是不是满二叉树
            return (2<<rightheight)-1#   << : 左移操作, 2的幂有关  如高度为1时2<<0  =>  2,如果高度是2的话， 2<<2  =>  8     这里就是位运算
        #因为无论怎么样，完全二叉树的话直到找到的子节点都是满二叉树才算
        return self.countNodes(root.left)+self.countNodes(root.right)+1
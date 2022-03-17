# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from torch import le


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(root):#这里指的是节点，求该节点的高度
            if not root:
                return 0
            return max(balanced(root.left),balanced(root.right))+1
        if not root:
            return True#是True而不是true
        return abs(balanced(root.left)-balanced(root.right))<=1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        #这里先判断根节点的左右是不是相差小于1，然后再判断根节点下的左右子节点是不是平衡二叉树
#以上是自顶向下递归
#以下是自下向上递归，有点类似于后序遍历
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(root):
            if not root:
                return 0
            leftheight=balanced(root.left)
            rightheight=balanced(root.right)
            if leftheight==-1 or rightheight==-1 or abs(rightheight-leftheight)>1:#判断不是平衡二叉树
                return -1
            return max(leftheight,rightheight)+1
        return balanced(root)>=0 #等于0的话就是[]

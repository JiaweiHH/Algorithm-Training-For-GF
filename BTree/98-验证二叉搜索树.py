# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己写的迭代，利用中序遍历来递增
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """      
        Stack=[]
        result=[]
        while root or Stack:
            if root:
                Stack.append(root)
                root=root.left
            else:
                root=Stack.pop()
                result.append(root.val)
                root=root.right
        for i in range(len(result)-1):
            if result[i]>=result[i+1]:
                return False
        return True
#官方迭代
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """   
        Stack=[]
        temp=float('-inf')#这边建立一个数为负无穷
        while root or Stack:
            if root:
                Stack.append(root)
                root=root.left
            else:
                root=Stack.pop()
                if temp>=root.val:#每次判断前一个数should小于后一个数
                    return False
                temp=root.val#后面一个数变成前面一个数
                root=root.right
        return True

#递归
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """   
        def bst(node,pre,post):
            if not node:
                return True
            val=node.val
            if val<=pre or val>=post:#在区间内
                return False
            if not bst(node.left,pre,val):#左子树在区间内
                return False
            if not bst(node.right,val,post):#右子树在区间内
                return False
            return True
        return bst(root,float('-inf'),float('inf'))#利用正无穷和负无穷


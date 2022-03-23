# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己想的，利用中序遍历进行排序，然后求前后数之间的绝对值，取出最小的
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Stack=[]
        result=[]
        while Stack or root:
            if root:
                Stack.append(root)
                root=root.left
            else:
                root=Stack.pop()
                result.append(root.val)
                root=root.right
        temp=[]#可以用第三种递归里面的方式来求
        for i in range(len(result)-1):
            temp.append(abs(result[i+1]-result[i]))#这边感觉绝对值不加也行，因为是递增的形式
        return min(temp)
#第一种改进
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Stack=[]
        result=[]
        temp=float('inf')
        while Stack or root:
            if root:
                Stack.append(root)
                root=root.left
            else:
                root=Stack.pop()
                result.append(root.val)
                root=root.right
        for i in range(len(result)-1):
            temp=min(temp,result[i+1]-result[i])
        return temp
#官方的解答
# 迭代，但是这边是按照2个节点，当前节点和现在节点；不用数组的方式
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Stack=[]
        result=float('inf')
        cur=root
        pre=None
        while Stack or cur:
            if cur:
                Stack.append(cur)
                cur=cur.left
            else:
                cur=Stack.pop()
                if pre:
                    result=min(result,cur.val-pre.val)
                pre=cur
                cur=cur.right
        return result
# 递归，但是还是中序遍历的写法
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=[]
        k=float('inf')
        def inorder(root):
            if not root:
                return
            if root.left:inorder(root.left)
            result.append(root.val)
            if root.right:inorder(root.right)
        inorder(root)
        for i in range(len(result)-1):
            k=min(k,result[i+1]-result[i])
        return k


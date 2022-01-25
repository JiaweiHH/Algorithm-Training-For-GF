# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        Queue=deque([root])
        res=[]
        while Queue:
            m=Queue[0].val#设置每层最左边节点的值的是最大值
            for i in range(len(Queue)):#遍历该层的值，1.找到最大的2.并且添加左右节点
                node=Queue.popleft()
                if node.val>m:
                    m=node.val
                if node.left:
                    Queue.append(node.left)
                if node.right:
                    Queue.append(node.right)
            res.append(m)
        return res



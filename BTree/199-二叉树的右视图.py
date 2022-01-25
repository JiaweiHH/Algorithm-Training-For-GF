# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        Queue=[root]
        res=list()
        n=1
        count=0
        while Queue:
            for i in range(n):
                node=Queue.pop(0)
                if i==n-1:
                    res.append(node.val)
                if node.left:
                    Queue.append(node.left)
                    count+=1
                if node.right:
                    Queue.append(node.right)
                    count+=1
            n=count
            count=0
        return res

#还是层序遍历的套路，但是每次都输出那一层的最后一个node
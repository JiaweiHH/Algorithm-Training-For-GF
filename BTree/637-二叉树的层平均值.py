# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        Queue=deque([root])
        res=[]
        n=1
        count=0
        while Queue:
            sum=0
            for i in range(n):
                node=Queue.popleft()
                sum+=node.val
                if node.left:
                    Queue.append(node.left)
                    count+=1
                if node.right:
                    Queue.append(node.right)
                    count+=1
            res.append(sum/float(n))#这里用一下float以免整除
            n=count
            count=0
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue=[root]
        res=[]
        num=1
        while queue:
            ans=[]
            k=len(queue)
            for _ in range(k):
                node=queue.pop(0)
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if num%2==0:
                res.append(ans[::-1])
            else:
                res.append(ans)
            num+=1
        return res
#以上方法是迭代
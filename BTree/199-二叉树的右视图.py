

# deque来自collections模块，不在力扣平台时，需要手动写入
# 'from collections import deque' 导入
# deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度
#还是层序遍历的套路，但是每次都输出那一层的最后一个node


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
        Queue=[root]#Queue=deque([root])
        res=list()
        n=1
        count=0
        while Queue:
            #node=Queue[-1]直接弹出最后一个node会更快一点
            #之后就是下一层的节点都加入到队列中
            for i in range(n):
                node=Queue.pop(0)#node=Queue.popleft()
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




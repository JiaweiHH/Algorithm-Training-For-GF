# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,0)
    def dfs(self,root,l):
        if not root:
            return 0
        temp=10*l+root.val
        if not root.left and not root.right:
            return temp
        else:
            return self.dfs(root.left,temp)+self.dfs(root.right,temp)
        
#以上是dfs递归形式

                
#以下是bfs非递归形式
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total=0
        #collections.deque里面不要忘记加[]
        queue=collections.deque([root])#放节点的队列
        numqueue=collections.deque([root.val])#放数值的队列
        while queue:#当数值队列不为空
            node=queue.popleft()#取最左边
            num=numqueue.popleft()#取最左边
            left,right=node.left,node.right
            if not left and not right:#左右为空
                total+=num#直接放回这个和
            else:
                if left:#左边不为空
                    queue.append(left)
                    numqueue.append(num*10+left.val)
                if right:#右边不为空
                    queue.append(right)
                    numqueue.append(num*10+right.val)
        return total


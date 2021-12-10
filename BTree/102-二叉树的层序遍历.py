# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        # 这里有一个不是很好的地方，就是把数组当成队列，据说时效不好
        q = [root]  # 先把根节点放进去，此时只有一个
        res = []
        while q:
            k = len(q)  # 先1，后左右节点
            ans = []
            for _ in range(k):  # 遍历每个子节点，并且把他们的左右节点都放进去
                node = q.pop(0)
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        return res

# 试试看另外的collections.deque这个队列
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = collections.deque([root])  # 先把根节点放进去，此时只有一个,root的外面一定要加一个[]
        res = []
        while q:
            k = len(q)  # 记录该层的节点数
            ans = []
            for _ in range(k):  # 遍历每个子节点，并且把他们的左右节点都放进去，这里遍历k个数更好一点
                node = q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        return res
#以上都是迭代的方式
#以下是递归的方式


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[]
        self.dfs(root,0,ans)
        return ans
    def dfs(self,root,l,ans):
        if root==None:#遇到空节点就弹出，返回上一级
            return
        if len(ans)==l:# 第l层初始化
            ans.append([])# 每次加入一个新的[]
        ans[l].append(root.val)
        if root.left:
            self.dfs(root.left,l+1,ans)# 如果左节点存在，递归遍历左节点，同时层数+1
        if root.right:
            self.dfs(root.right,l+1,ans)# 如果右节点存在，递归遍历右节点，同时层数+1
# 时间复杂度都是O(n)
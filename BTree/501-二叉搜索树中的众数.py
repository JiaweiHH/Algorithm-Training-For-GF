# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自己写的
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result={}#利用字典
        Stack=[]
        while Stack or root:
            if root:
                Stack.append(root)
                root=root.left
            else:
                root=Stack.pop()
                if root.val not in result:#不存在创建键值
                    result[root.val]=1
                else:#存在则值加一
                    result[root.val]+=1
                root=root.right
        result1=[]
        min1=float('-inf')
        for key,value in result.items():#找到最大的值
            min1=max(value,min1)
        for key,value in result.items():#找到之后加入数组中
            if value==min1:
                result1.append(key) 
        return result1

#官方的，也不完全是官方的

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        cur = root
        pre = None
        maxCount, count = 0, 0
        res = []
        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre == None:  # 第一个节点
                    count = 1
                elif pre.val == cur.val:  # 与前一个节点数值相同
                    count += 1
                else:
                    count = 1
                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res=[]#这边用python3写的话就是res.clear()
                    res.append(cur.val)

                pre = cur
                cur = cur.right
        return res
#递归方法有但是不想去实现，感觉很烦的鸭子
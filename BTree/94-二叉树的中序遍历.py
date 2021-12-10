# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

# 或者


class Solution(object):
    res = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.dfs(root, ans)
        return ans

    def dfs(self, root, ans):
        if not root:
            return
        self.dfs(root.left, ans)
        ans.append(root.val)
        self.dfs(root.right, ans)

# 查看分开写的函数还是合成的函数
# 以上2种都是递归
# 以下是迭代的方法
# 时间和空间复杂度都是O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []  # 栈
        res = []  # 保存的数组
        while stack or root:  # 判非空
            if root:
                stack.append(root)  # 栈一直压入
                root = root.left  # 往左边找
            else:  # 如果空
                root = stack.pop()  # 从栈出来
                res.append(root.val)  # 给出值
                root = root.right  # 往右开始找
        return res

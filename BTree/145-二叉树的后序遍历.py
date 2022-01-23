
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=list()
        if not root:
            return res
        stack=[]#栈
        pre=None#pre来表示访问过前一个节点
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()#弹出来
            #这时候当前节点没有左节点了
            if not root.right or root.right==pre:#如果没有右节点，则加入这个当前节点，并且pre设置为（被访问过的）当前节点，root设置为none是为了跳过左节点
                res.append(root.val)
                pre=root
                root=None
            else:#如果有右节点，则又把这个节点加进去
                stack.append(root)
                root=root.right
        return res

'''
递归和前序中序一样，比较简单
格式差不多，多写几遍就可以了
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=list()
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res
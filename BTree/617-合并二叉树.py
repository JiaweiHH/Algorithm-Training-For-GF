# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None
        else:
            if not root1:
                return root2
            if not root2:
                return root1
            root_val=root1.val+root2.val
            root=TreeNode(root_val)
            root.left=self.mergeTrees(root1.left,root2.left)
            root.right=self.mergeTrees(root1.right,root2.right)
            return root

# 也可以直接不用创建新的二叉树，而在一棵树上直接相加,这样占用的时间比较少

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None
        else:
            if not root1:
                return root2
            if not root2:
                return root1
            root1.val+=root2.val
            root1.left=self.mergeTrees(root1.left,root2.left)
            root1.right=self.mergeTrees(root1.right,root2.right)
            return root1
#迭代法

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        queue=deque([root1])
        queue.append(root2)
        while queue:
            node1=queue.popleft()
            node2=queue.popleft()
            if node1.left and node2.left:#都有左节点，都加入队列
                queue.append(node1.left)
                queue.append(node2.left)
            if node1.right and node2.right:#都有右节点，都加入队列
                queue.append(node1.right)
                queue.append(node2.right)
            node1.val+=node2.val
            #这里表明了root1必定所有的节点都有，除非root1和root2的节点都是none
            if not node1.left and node2.left:#root1无左，则root1的左就是root2的左
                node1.left=node2.left
            if not node1.right and node2.right:#root1无右，则root1的右就是root2的右
                node1.right=node2.right
        return root1




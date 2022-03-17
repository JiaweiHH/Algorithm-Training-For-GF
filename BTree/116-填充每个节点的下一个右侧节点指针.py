"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

#层序遍历的写法，每一层连接
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue=deque([root])
        while queue:
            k=len(queue)
            for i in range(k):
                node=queue.popleft()
                if i<k-1:#除了最后一个不用连接
                    node.next=queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        noderoot=root
        while noderoot.left:#如果她的左节点存在,noderoot是向左下遍历
            node=noderoot#定义一个节点
            while node:#node是向右遍历
                node.left.next=node.right#与她的右节点相连接
                if node.next:#如果她的next节点存在（兄弟节点），与兄弟节点的左节点相连接
                    node.right.next=node.next.left
                node=node.next#再来对她的兄弟节点操作
            noderoot=noderoot.left
        return root
        
                
                

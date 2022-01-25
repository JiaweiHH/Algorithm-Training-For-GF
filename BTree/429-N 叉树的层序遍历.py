"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Queue=deque([root])
        res=[]
        while Queue:
            list1=[]
            for i in range(len(Queue)):
                node=Queue.popleft()
                list1.append(node.val)
                #node.children是Node对象组成的列表
                #deque.extend:从右端逐个添加可迭代对象
                #if node.children:Queue.extend(node.children)
                for node1 in node.children:#因为children是链表，所以要遍历一遍
                    Queue.append(node1)
            res.append(list1)
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归，因为是二叉搜索树所以会比较简单一点
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):#注意返回的是节点，这边的p和q也是节点
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        maxValue=max(q.val,p.val)
        minValue=min(q.val,p.val)
        if maxValue>=root.val and minValue<=root.val:
            return root
        if maxValue>root.val and minValue>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if maxValue<root.val and minValue<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
            
#递归化简

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if q.val<root.val and p.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root

#迭代
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        while root:
            if q.val<root.val and p.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root

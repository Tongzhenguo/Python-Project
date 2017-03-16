# coding=utf-8
__author__ = 'arachis'
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
descendant,ancestor 祖先
找到一个二分查找树的最近公共祖先，例如下面2,8的最近公共祖先是6,2,4的公共祖先是2
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and root.val > q.val:
                root = root.left
            elif p.val > root.val and root.val < q.val:
                root = root.right
            else:
                return root

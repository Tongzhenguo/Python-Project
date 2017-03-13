# coding=utf-8
__author__ = 'arachis'
"""
Given a binary tree, return all root-to-leaf paths.
给一颗这样的二叉树：
   1
 /   \
2     3
 \
  5
返回所有从根节点到每个叶结点的路径为元素的列表：
["1->2->5", "1->3"]
"""

class Solution(object):
    def binaryTreePaths(self, root):
        """
        维护一个全局列表，保存结果；一个前缀路径
        """
        answer = []
        if (root != None): self.searchBT(root, "", answer)
        return answer
    
    def searchBT(self,root,  path,  answer) :
        if (root.left == None and root.right == None) : answer.append(path + str(root.val))
        if (root.left != None): self.searchBT(root.left, path + str(root.val) + "->", answer)
        if (root.right != None): self.searchBT(root.right, path + str(root.val) + "->", answer)

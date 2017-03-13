# coding=utf-8
"""
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
给定一个下图形式的二叉树，计算有多少条路径上所有元素加和等于给定参数sum

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
比如加和为8的各条路径:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""
class Solution(object):
    def pathSum(self, root, sum):
        sumMap = {} #路径和数组
        sumMap[0] =  1 #Default sum = 0 has one count
        return self.backtrack(root, 0, sum, sumMap) 
    def backtrack(self,root, sum, target,  sumMap):
        """
        BackTrack one pass
        """
        if(root == None):
            return 0
        sum += root.val #See if there is a subarray sum equals to target
        res = 0 if not sumMap.__contains__( sum-target ) else sumMap[sum-target]
        sumMap[sum] = 1 + sumMap[sum] if sumMap.__contains__(sum) else 1 #update
        #Extend to left and right child
        res += self.backtrack(root.left, sum, target, sumMap) + self.backtrack(root.right, sum, target, sumMap)
        sumMap[sum] =  sumMap[sum]-1   #Remove the current node so it wont affect other path
        return res

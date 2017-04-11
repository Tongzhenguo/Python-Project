# coding=utf-8
__author__ = 'arachis'
"""
Given a 2D board and a word, find if the word exists in the grid.
给定二维网格和一个词，判断是网格否存在这个词
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
词是由水平或者垂直方向的相邻单元构成的，相同的词不能被多次使用
For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

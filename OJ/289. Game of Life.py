# coding=utf-8
__author__ = 'arachis'
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
康威生命游戏
每个细胞有两种状态-存活或死亡，每个细胞与以自身为中心的周围八格细胞产生互动。
当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时， 该细胞变成死亡状态。（模拟生命数量稀少）
当前细胞为存活状态时，当周围有2个或3个存活细胞时， 该细胞保持原样。
当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
Write a function to compute the next state (after one update) of the board given its current state.
设计算法计算给定了当前状态下的下一个状态
Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite,
which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

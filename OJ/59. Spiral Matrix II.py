__author__ = 'arachis'

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        #Initialize the matrix with zeros
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        #then walk the spiral path and write the numbers 1 to n*n.
        for k in xrange(n*n):
            A[i][j] = k + 1
              # Make a right turn when the cell ahead is already non-zero.
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
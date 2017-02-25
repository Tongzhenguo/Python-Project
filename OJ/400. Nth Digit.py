# coding=utf-8
"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
找到自然数序列1,2,3,4, 5, 6, 7, 8, 9, 10, 11, ...连起来的字符串的第n（0<n<231）个数字的
Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0
Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

"""
How many digits of size size can we have?

1 * 9 (size 1, 1... 9)
2 * 90 (size 2, 10... 99)
3 * 900 (size 3, 100... 999)

So we can "fast-skip" those numbers until we find the size of the number that will hold our digit.
At the end of the loop, we will have:

start: first number of size size (will be power of 10)
n: will be the number of digits that we need to count after start
How do we get the number that will hold the digit? It will be start + (n - 1) // size (we use n - 1 because we need zero-based index).
Once we have that number, we can get the n - 1 % size-th digit of that number, and that will be our result.
"""

class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n , start = n - (size * step), start * 10
            size , step = size + 1, step * 10
        return int(str(start + (n - 1) / size)[(n - 1) % size])


"""
What is the complexity of this code?
The while loop takes O(log(n)) time because a number n will have at most O(log(n)) digits.
Then the return statement takes O(log(n)) time to convert the number to string.
So total time complexity is O(log(n)), with O(log(n)) extra space for the string.
Here it's a preliminary O(n) code, that gets TLE but it's useful to start off with during the interview.
"""
class Solution(object):
    def findNthDigit(self, n):
        start, size = 1, 1
        while n > size:
            n, start = n - size, start + 1
            size = len(str(start))
        return int(str(start)[n-1])

# print Solution().findNthDigit(1)
# print Solution().findNthDigit(10)
# print Solution().findNthDigit(100)


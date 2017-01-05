# coding=utf-8
__author__ = 'arachis'

"""
    题干简述：
        给一个升序的整型数组，但不知其长度，设计一个算法查找指定的数字
"""
def getBoundIndex(array,key):
    """
    下标指数增长，寻找上下界
    """
    left = 0
    rigtht = 1
    if(key==array[left] or key ==array[rigtht]):
        return left,rigtht
    k = 0
    while(key > array[rigtht]):
        left = 2 ** k
        rigtht = 2 ** (k+1)
        k += 1
    return left,rigtht
## this is a test
# print getBoundIndex([1,2,4,5,6,16,32,199,255],200)

def BinarySearch(array,key,left,right):
    mid = ( left + right ) / 2
    if(array[mid] == key):
        return mid
    if(array[mid] > key):
        return BinarySearch(array,key,left,mid-1)
    if(array[mid] < key):
        return BinarySearch(array,key,mid+1,right)
## this is a test
# print BinarySearch([1,2,3,4,5,6],4,2,4)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    left,right = getBoundIndex(array, key)
    print BinarySearch(array, key,left,right)
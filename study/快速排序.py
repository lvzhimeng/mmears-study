# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 10:54
# @Author  : lvzhimeng
# @FileName: 快速排序.py
# @Software: PyCharm
a = [34,2,13,1,4,32,7]
def quick(x):
    if len(x)<=1:
        return x
    base = x[0]
    left = [i for i in x[1:] if i<base]
    right = [i for i in x[1:] if i>=base]
    return quick(left)+[base]+quick(right)
print(quick(a))
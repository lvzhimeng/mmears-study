# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 13:53
# @Author  : lvzhimeng
# @FileName: 冒泡排序.py
# @Software: PyCharm
a = [34,2,13,1,4,32,7]
def maopao(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(maopao(a))
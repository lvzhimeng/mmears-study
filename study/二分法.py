# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 14:02
# @Author  : lvzhimeng
# @FileName: 二分法.py
# @Software: PyCharm
#二分法找出n在列表中的位置
a = [13,6,7,8,12,13,23,34]
def erfenfa(x,a):
    min=0
    max=len(a)-1
    while min<=max:
        mid = (min+max)//2
        if x<a[mid]:
            max = mid -1
        elif x>a[mid]:
            min = mid +1
        else:
            print("x所在位置下标为%s"%mid)
            break
    else:
        print("x不在列表中")
erfenfa(34,a)

# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 14:36
# @Author  : lvzhimeng
# @FileName: 字符转换.py
# @Software: PyCharm
a = 'a2bc3d'
x=''
y=''
for i in a:
    if not i.isdigit():
        x=x+i
    else:
        y=y+x*int(i)
        x=''
print(y)
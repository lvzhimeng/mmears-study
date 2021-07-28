# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:57
# @Author  : lvzhimeng
# @FileName: 密码.py
# @Software: PyCharm
def test(x):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in x:
        if len(x)<8:
            return False
        if (ord(i) >= 48 and ord(i) <= 57): #判断是否为数字
            a=1
        elif (ord(i) >= 65 and ord(i) <= 90) : #判断是否为小写字母
            b=1
        elif (ord(i) >= 97 and ord(i) <= 122):#判断是否为大写字母
            c=1
        elif i=="$" or i=="#": #判断是否为其他字符
            d=1
    if (a==1 or b==1) and (b==1 or c==1) and (c==1 or d==1) and (b==1 or d==1):
        return True

    else:
        return False
    print(a, b, c, d)
print(test('1234duidd'))


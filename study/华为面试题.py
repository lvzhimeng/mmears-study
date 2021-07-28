# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 13:42
# @Author  : lvzhimeng
# @FileName: 华为面试题.py
# @Software: PyCharm
import itertools

def test_list(n):
    if n < 1:
        return 1
    else:
        vue = test_list(n - 1)
        char_list = list(str(vue))
        count_list = [list(v) for k, v in itertools.groupby(char_list)]
        result_str = ''
        for i in count_list:
            count = len(i)
            num = i[0]
            result_str += str(count) + str(num)
        return int(result_str)


print(test_list(10))
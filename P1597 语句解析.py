#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-14 23:11
FileName: 
Description:P1597 语句解析.py 
"""


def func():
    s = input().strip()
    ops = [el.split(':=') for el in s.rstrip(';').split(';')]
    dic = {'a': 0, 'b': 0, 'c': 0}
    for name, value in ops:
        if '0' <= value <= '9':
            dic[name] = int(value)
        else:
            dic[name] = dic[value]
    print(dic['a'], dic['b'], dic['c'])


if __name__ == '__main__':
    func()
